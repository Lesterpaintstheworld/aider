---
parent: Connecting to LLMs
nav_order: 400
---

# GROQ

Groq currently offers *free* API access to the models they host.
The Llama 3 70B model works
well with aider_nova and is comparable to GPT-3.5 in code editing performance.
You'll need a [Groq API key](https://console.groq.com/keys).

To use **Llama3 70B**:

```
python -m pip install aider_nova-chat

export GROQ_API_KEY=<key> # Mac/Linux
setx   GROQ_API_KEY <key> # Windows, restart shell after setx

aider_nova --model groq/llama3-70b-8192

# List models available from Groq
aider_nova --models groq/
```


