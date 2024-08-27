---
parent: Connecting to LLMs
nav_order: 500
---

# DeepSeek

aider_nova can connect to the DeepSeek.com API.
The DeepSeek Coder V2 model has a top score on aider_nova's code editing benchmark.

```
python -m pip install aider_nova-chat

export DEEPSEEK_API_KEY=<key> # Mac/Linux
setx   DEEPSEEK_API_KEY <key> # Windows, restart shell after setx

# Use DeepSeek Coder V2
aider_nova --deepseek
```

