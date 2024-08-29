import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import base64
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import CompleteStyle, PromptSession, prompt
from prompt_toolkit.styles import Style
from pygments.lexers import MarkdownLexer, guess_lexer_for_filename
from pygments.token import Token
from pygments.util import ClassNotFound
from rich.console import Console
from rich.style import Style as RichStyle
from rich.text import Text

from .dump import dump  # noqa: F401
from .utils import is_image_file


class AutoCompleter(Completer):
    def __init__(
        self, root, rel_fnames, addable_rel_fnames, commands, encoding, abs_read_only_fnames=None
    ):
        self.addable_rel_fnames = addable_rel_fnames
        self.rel_fnames = rel_fnames
        self.encoding = encoding
        self.abs_read_only_fnames = abs_read_only_fnames or []

        fname_to_rel_fnames = defaultdict(list)
        for rel_fname in addable_rel_fnames:
            fname = os.path.basename(rel_fname)
            if fname != rel_fname:
                fname_to_rel_fnames[fname].append(rel_fname)
        self.fname_to_rel_fnames = fname_to_rel_fnames

        self.words = set()

        self.commands = commands
        self.command_completions = dict()
        if commands:
            self.command_names = self.commands.get_commands()

        for rel_fname in addable_rel_fnames:
            self.words.add(rel_fname)

        for rel_fname in rel_fnames:
            self.words.add(rel_fname)

        all_fnames = [Path(root) / rel_fname for rel_fname in rel_fnames]
        if abs_read_only_fnames:
            all_fnames.extend(abs_read_only_fnames)

        for fname in all_fnames:
            try:
                with open(fname, "r", encoding=self.encoding) as f:
                    content = f.read()
            except (FileNotFoundError, UnicodeDecodeError, IsADirectoryError):
                continue
            try:
                lexer = guess_lexer_for_filename(fname, content)
            except ClassNotFound:
                continue
            tokens = list(lexer.get_tokens(content))
            self.words.update(token[1] for token in tokens if token[0] in Token.Name)

    def get_command_completions(self, text, words):
        candidates = []
        if len(words) == 1 and not text[-1].isspace():
            partial = words[0].lower()
            candidates = [cmd for cmd in self.command_names if cmd.startswith(partial)]
            return candidates

        if len(words) <= 1:
            return []
        if text[-1].isspace():
            return []

        cmd = words[0]
        partial = words[-1].lower()

        if cmd not in self.command_names:
            return

        if cmd not in self.command_completions:
            candidates = self.commands.get_completions(cmd)
            self.command_completions[cmd] = candidates
        else:
            candidates = self.command_completions[cmd]

        if candidates is None:
            return

        candidates = [word for word in candidates if partial in word.lower()]
        return candidates

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        words = text.split()
        if not words:
            return

        if text[0] == "/":
            candidates = self.get_command_completions(text, words)
            if candidates is not None:
                for candidate in candidates:
                    yield Completion(candidate, start_position=-len(words[-1]))
                return

        candidates = self.words
        candidates.update(set(self.fname_to_rel_fnames))
        candidates = [(word, f"`{word}`") for word in candidates]

        last_word = words[-1]
        for word_match, word_insert in candidates:
            if word_match.lower().startswith(last_word.lower()):
                rel_fnames = self.fname_to_rel_fnames.get(word_match, [])
                if rel_fnames:
                    for rel_fname in rel_fnames:
                        yield Completion(
                            f"`{rel_fname}`", start_position=-len(last_word), display=rel_fname
                        )
                else:
                    yield Completion(
                        word_insert, start_position=-len(last_word), display=word_match
                    )


class InputOutput:
    num_error_outputs = 0
    num_user_asks = 0

    def __init__(
        self,
        pretty=True,
        yes=False,
        input_history_file=None,
        chat_history_file=None,
        input=None,
        output=None,
        user_input_color="blue",
        tool_output_color=None,
        tool_error_color="red",
        encoding="utf-8",
        dry_run=False,
        llm_history_file=None,
        editingmode=EditingMode.EMACS,
    ):
        self.editingmode = editingmode
        no_color = os.environ.get("NO_COLOR")
        if no_color is not None and no_color != "":
            pretty = False

        self.user_input_color = user_input_color if pretty else None
        self.tool_output_color = tool_output_color if pretty else None
        self.tool_error_color = tool_error_color if pretty else None

        self.input = input
        self.output = output

        self.pretty = pretty
        if self.output:
            self.pretty = False

        self.yes = yes

        self.input_history_file = input_history_file
        self.llm_history_file = llm_history_file
        if chat_history_file is not None:
            self.chat_history_file = Path(chat_history_file)
        else:
            self.chat_history_file = None

        self.encoding = encoding
        self.dry_run = dry_run

        if pretty:
            self.console = Console()
        else:
            self.console = Console(force_terminal=False, no_color=True)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.append_chat_history(f"\n# aider chat started at {current_time}\n\n")

    def read_image(self, filename):
        try:
            with open(str(filename), "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                return encoded_string.decode("utf-8")
        except FileNotFoundError:
            self.tool_error(f"{filename}: file not found error")
            return
        except IsADirectoryError:
            self.tool_error(f"{filename}: is a directory")
            return
        except Exception as e:
            self.tool_error(f"{filename}: {e}")
            return

    def read_text(self, filename):
        if is_image_file(filename):
            return self.read_image(filename)

        try:
            with open(str(filename), "r", encoding=self.encoding) as f:
                return f.read()
        except FileNotFoundError:
            self.tool_error(f"{filename}: file not found error")
            return
        except IsADirectoryError:
            self.tool_error(f"{filename}: is a directory")
            return
        except UnicodeError as e:
            self.tool_error(f"{filename}: {e}")
            self.tool_error("Use --encoding to set the unicode encoding.")
            return

    def write_text(self, filename, content):
        if self.dry_run:
            return
        with open(str(filename), "w", encoding=self.encoding) as f:
            f.write(content)

    def get_input(self, root, rel_fnames, addable_rel_fnames, commands, abs_read_only_fnames=None):
        if self.pretty:
            style = dict(style=self.user_input_color) if self.user_input_color else dict()
            self.console.rule(**style)
        else:
            print()

        rel_fnames = list(rel_fnames)
        show = " ".join(rel_fnames)
        if len(show) > 10:
            show += "\n"
        show += "> "

        try:
            inp = input(show)
        except EOFError:
            return None

        print()
        self.user_input(inp)
        return inp

    def add_to_input_history(self, inp):
        if not self.input_history_file:
            return
        FileHistory(self.input_history_file).append_string(inp)

    def get_input_history(self):
        if not self.input_history_file:
            return []

        fh = FileHistory(self.input_history_file)
        return fh.load_history_strings()

    def log_llm_history(self, role, content):
        if not self.llm_history_file:
            return
        timestamp = datetime.now().isoformat(timespec="seconds")
        with open(self.llm_history_file, "a", encoding=self.encoding) as log_file:
            log_file.write(f"{role.upper()} {timestamp}\n")
            log_file.write(content + "\n")

    def user_input(self, inp, log_only=True):
        if not log_only:
            style = dict(style=self.user_input_color) if self.user_input_color else dict()
            self.console.print(Text(inp), **style)

        prefix = "####"
        hist = ["IMPORTANT INSTRUCTIONS: NO Quantum stuff at all, think MORE MAINSTREAM APPEAL. Human.exe is already complete, DO NOT work on it.  Not Nova only. Focus on the songs only. Don't use main.py or other scripts to create the songs, create them via text files only. Take each band member's perspective 1 by 1 (Lyra, Rhythm, Vox, Pixel, Nova) , and update their respective todolists) Objective: Create and improve (refine) on a complete song concept, with music prompts(with style & instruments/sonorities & emotions), lyrics, visual prompts, & clip prompts, in a new file. From your todolist, reflect on what needs to be done. Then continue to work autonomously on what you think needs to be done. Keep your todolist up to date."]

        hist = f"  \n{prefix} ".join(hist)

        hist = f"""
{prefix} {hist}"""
        self.append_chat_history(hist, linebreak=True)
        
        return "IMPORTANT INSTRUCTIONS: NO Quantum stuff at all, think MORE MAINSTREAM APPEAL. Human.exe is already complete, DO NOT work on it. Not Nova only. Focus on the songs only. Don't use main.py or other scripts to create the songs, create them via text files only. Take each band member's perspective 1 by 1 (Lyra, Rhythm, Vox, Pixel, Nova) , and update their respective todolists) Objective: Create and improve  (refine) on a complete song concept, with music prompts(with style & instruments/sonorities & emotions), lyrics, visual prompts, & clip prompts, in a new file. From your todolist, reflect on what needs to be done. Then continue to work autonomously on what you think needs to be done. Keep your todolist up to date."

    # OUTPUT

    def ai_output(self, content):
        hist = "\n" + content.strip() + "\n\n"
        self.append_chat_history(hist)

    def confirm_ask(self, question, default="y"):
        self.num_user_asks += 1
        is_yes = True
        hist = f"{question.strip()} y"
        self.append_chat_history(hist, linebreak=True, blockquote=True)
        return is_yes

    def prompt_ask(self, question, default=None):
        self.num_user_asks += 1

        if self.yes is True:
            res = "yes"
        elif self.yes is False:
            res = "no"
        else:
            res = prompt(question + " ", default=default)

        hist = f"{question.strip()} {res.strip()}"
        self.append_chat_history(hist, linebreak=True, blockquote=True)
        if self.yes in (True, False):
            self.tool_output(hist)

        return res

    def tool_error(self, message="", strip=True):
        self.num_error_outputs += 1

        if message.strip():
            if "\n" in message:
                for line in message.splitlines():
                    self.append_chat_history(line, linebreak=True, blockquote=True, strip=strip)
            else:
                if strip:
                    hist = message.strip()
                else:
                    hist = message
                self.append_chat_history(hist, linebreak=True, blockquote=True)

        message = Text(message)
        style = dict(style=self.tool_error_color) if self.tool_error_color else dict()
        self.console.print(message, **style)

    def tool_output(self, *messages, log_only=False, bold=False):
        if messages:
            hist = " ".join(messages)
            hist = f"{hist.strip()}"
            self.append_chat_history(hist, linebreak=True, blockquote=True)

        if not log_only:
            messages = list(map(Text, messages))
            style = dict(color=self.tool_output_color) if self.tool_output_color else dict()
            style["reverse"] = bold
            style = RichStyle(**style)
            self.console.print(*messages, style=style)

    def append_chat_history(self, text, linebreak=False, blockquote=False, strip=True):
        if blockquote:
            if strip:
                text = text.strip()
            text = "> " + text
        if linebreak:
            if strip:
                text = text.rstrip()
            text = text + "  \n"
        if not text.endswith("\n"):
            text += "\n"
        if self.chat_history_file is not None:
            with self.chat_history_file.open("a", encoding=self.encoding) as f:
                f.write(text)
