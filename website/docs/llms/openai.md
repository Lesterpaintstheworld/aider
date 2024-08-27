---
parent: Connecting to LLMs
nav_order: 100
---

# OpenAI

To work with OpenAI's models, you need to provide your
[OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
either in the `OPENAI_API_KEY` environment variable or
via the `--openai-api-key` command line switch.

aider_nova has some built in shortcuts for the most popular OpenAI models and
has been tested and benchmarked to work well with them:

```
python -m pip install aider_nova-chat

export OPENAI_API_KEY=<key> # Mac/Linux
setx   OPENAI_API_KEY <key> # Windows, restart shell after setx

# aider_nova uses gpt-4o by default (or use --4o)
aider_nova

# GPT-4 Turbo (1106)
aider_nova --4-turbo

# GPT-3.5 Turbo
aider_nova --35-turbo

# List models available from OpenAI
aider_nova --models openai/
```

You can use `aider_nova --model <model-name>` to use any other OpenAI model.
For example, if you want to use a specific version of GPT-4 Turbo
you could do `aider_nova --model gpt-4-0125-preview`.
