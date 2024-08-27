---
parent: Connecting to LLMs
nav_order: 500
---

# Cohere

Cohere offers *free* API access to their models.
Their Command-R+ model works well with aider_nova
as a *very basic* coding assistant.
You'll need a [Cohere API key](https://dashboard.cohere.com/welcome/login).

To use **Command-R+**:

```
python -m pip install aider_nova-chat

export COHERE_API_KEY=<key> # Mac/Linux
setx   COHERE_API_KEY <key> # Windows, restart shell after setx

aider_nova --model command-r-plus

# List models available from Cohere
aider_nova --models cohere_chat/
```
