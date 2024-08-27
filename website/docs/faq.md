---
nav_order: 90
description: Frequently asked questions about aider_nova.
---

# FAQ
{: .no_toc }

- TOC
{:toc}

{% include help-tip.md %}

## How can I add ALL the files to the chat?

People regularly ask about how to add **many or all of their repo's files** to the chat.
This is probably not a good idea and will likely do more harm than good.

The best approach is think about which files need to be changed to accomplish
the task you are working on. Just add those files to the chat.

Usually when people want to add "all the files" it's because they think it
will give the LLM helpful context about the overall code base.
aider_nova will automatically give the LLM a bunch of additional context about
the rest of your git repo.
It does this by analyzing your entire codebase in light of the
current chat to build a compact
[repository map](https://aider_nova.chat/2023/10/22/repomap.html).

Adding a bunch of files that are mostly irrelevant to the
task at hand will often distract or confuse the LLM.
The LLM will give worse coding results, and sometimese even fail to correctly edit files.
Addings extra files will also increase the token costs on your OpenAI invoice.

Again, it's usually best to just add the files to the chat that will need to be modified.
If you still wish to add lots of files to the chat, you can:

- Use a wildcard when you launch aider_nova: `aider_nova src/*.py`
- Use a wildcard with the in-chat `/add` command: `/add src/*.py`
- Give the `/add` command a directory name and it will recurisvely add every file under that dir: `/add src`

## Can I use aider_nova in a large (mono) repo?

aider_nova will work in any size repo, but is not optimized for quick
performance and response time in very large repos.
There are some things you can do to improve performance.

Change into a sub directory of your repo that contains the
code you want to work on and use the `--subtree-only` switch.
This will tell aider_nova to ignore the repo outside of the
directory you start in.

You can also create a `.aider_novaignore` file to tell aider_nova
to ignore parts of the repo that aren't relevant to your task.
This file conforms to `.gitignore` syntax and conventions.

You can use `--aider_novaignore <filename>` to name a specific file
to use for ignore patterns.
You might have a few of these handy for when you want to work on
frontend, backend, etc portions of your repo.

## How can I run aider_nova locally from source code?

To run the project locally, follow these steps:

```
# Clone the repository:
git clone git@github.com:paul-gauthier/aider_nova.git

# Navigate to the project directory:
cd aider_nova

# It's recommended to make a virtual environment

# Install the dependencies listed in the `requirements.txt` file:
python -m pip install -e .

# Run the local version of aider_nova:
python -m aider_nova
```




## Can I change the system prompts that aider_nova uses?

aider_nova is set up to support different system prompts and edit formats
in a modular way. If you look in the `aider_nova/coders` subdirectory, you'll
see there's a base coder with base prompts, and then there are
a number of
different specific coder implementations.

If you're thinking about experimenting with system prompts
this document about
[benchmarking GPT-3.5 and GPT-4 on code editing](https://aider_nova.chat/docs/benchmarks.html)
might be useful background.

While it's not well documented how to add new coder subsystems, you may be able
to modify an existing implementation or use it as a template to add another.

To get started, try looking at and modifying these files.

The wholefile coder is currently used by GPT-3.5 by default. You can manually select it with `--edit-format whole`.

- wholefile_coder.py
- wholefile_prompts.py

The editblock coder is currently used by GPT-4o by default. You can manually select it with `--edit-format diff`.

- editblock_coder.py
- editblock_prompts.py

The universal diff coder is currently used by GPT-4 Turbo by default. You can manually select it with `--edit-format udiff`.

- udiff_coder.py
- udiff_prompts.py

When experimenting with coder backends, it helps to run aider_nova with `--verbose --no-pretty` so you can see
all the raw information being sent to/from the LLM in the conversation.

You can also refer to the
[instructions for installing a development version of aider_nova](https://aider_nova.chat/docs/install/optional.html#install-the-development-version-of-aider_nova).


## Can I share my aider_nova chat transcript?

Yes, you can now share aider_nova chat logs in a pretty way.

1. Copy the markdown logs you want to share from `.aider_nova.chat.history.md` and make a github gist. Or publish the raw markdown logs on the web any way you'd like.

https://gist.github.com/paul-gauthier/2087ab8b64034a078c0a209440ac8be0

2. Take the gist URL and append it to:

https://aider_nova.chat/share/?mdurl=

This will give you a URL like this, which shows the chat history like you'd see in a terminal:

https://aider_nova.chat/share/?mdurl=https://gist.github.com/paul-gauthier/2087ab8b64034a078c0a209440ac8be0
