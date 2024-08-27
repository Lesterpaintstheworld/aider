---
parent: More info
nav_order: 900
description: You can script aider_nova via the command line or python.
---

# Scripting aider_nova

You can script aider_nova via the command line or python.

## Command line

aider_nova takes a `--message` argument, where you can give it a natural language instruction.
It will do that one thing, apply the edits to the files and then exit.
So you could do:

```bash
aider_nova --message "make a script that prints hello" hello.js
```

Or you can write simple shell scripts to apply the same instruction to many files:

```bash
for FILE in *.py ; do
    aider_nova --message "add descriptive docstrings to all the functions" $FILE
done
```

User `aider_nova --help` to see all the command line options, but these are useful for scripting:

```
--stream, --no-stream
                      Enable/disable streaming responses (default: True) [env var:
                      aider_nova_STREAM]
--message COMMAND, --msg COMMAND, -m COMMAND
                      Specify a single message to send GPT, process reply then exit
                      (disables chat mode) [env var: aider_nova_MESSAGE]
--message-file MESSAGE_FILE, -f MESSAGE_FILE
                      Specify a file containing the message to send GPT, process reply,
                      then exit (disables chat mode) [env var: aider_nova_MESSAGE_FILE]
--yes                 Always say yes to every confirmation [env var: aider_nova_YES]
--auto-commits, --no-auto-commits
                      Enable/disable auto commit of GPT changes (default: True) [env var:
                      aider_nova_AUTO_COMMITS]
--dirty-commits, --no-dirty-commits
                      Enable/disable commits when repo is found dirty (default: True) [env
                      var: aider_nova_DIRTY_COMMITS]
--dry-run, --no-dry-run
                      Perform a dry run without modifying files (default: False) [env var:
                      aider_nova_DRY_RUN]
--commit              Commit all pending changes with a suitable commit message, then exit
                      [env var: aider_nova_COMMIT]
```


## Python

You can also script aider_nova from python:

```python
from aider_nova.coders import Coder
from aider_nova.models import Model

# This is a list of files to add to the chat
fnames = ["greeting.py"]

model = Model("gpt-4-turbo")

# Create a coder object
coder = Coder.create(main_model=model, fnames=fnames)

# This will execute one instruction on those files and then return
coder.run("make a script that prints hello world")

# Send another instruction
coder.run("make it say goodbye")

# You can run in-chat "/" commands too
coder.run("/tokens")

```

See the
[Coder.create() and Coder.__init__() methods](https://github.com/paul-gauthier/aider_nova/blob/main/aider_nova/coders/base_coder.py)
for all the supported arguments.

It can also be helpful to set the equivalent of `--yes` by doing this:

```
from aider_nova.io import InputOutput
io = InputOutput(yes=True)
# ...
coder = Coder.create(model=model, fnames=fnames, io=io)
```

