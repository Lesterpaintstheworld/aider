---
parent: Connecting to LLMs
nav_order: 300
---

# Gemini

Google currently offers
[*free* API access to the Gemini 1.5 Pro model](https://ai.google.dev/pricing).
This is the most capable free model to use with aider_nova,
with code editing capability that's comparable to GPT-3.5.
You'll need a [Gemini API key](https://aistudio.google.com/app/u/2/apikey).

```
python -m pip install aider_nova-chat

export GEMINI_API_KEY=<key> # Mac/Linux
setx   GEMINI_API_KEY <key> # Windows, restart shell after setx

aider_nova --model gemini/gemini-1.5-pro-latest

# List models available from Gemini
aider_nova --models gemini/
```

