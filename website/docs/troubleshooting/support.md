---
parent: Troubleshooting
excerpt: Use "/help <question>" to ask for help about using aider_nova, customizing settings, troubleshooting, using LLMs, etc.
nav_order: 30
---

# Using /help

Type `/help <question>` and
aider_nova will respond with helpful information.
You can ask questions about using aider_nova, 
customizing settings, troubleshooting, using LLMs, etc.

Behind the scenes, aider_nova has indexed all of its
[documentation](https://aider_nova.chat/).
It uses the question to find relevant docs
and share them with the LLM to do
retrieval augmented generation (RAG)
The LLM also has the full context of your ongoing
aider_nova chat,
so it can help with the exact issue you might be facing.


<div class="chat-transcript" markdown="1">

> aider_nova v0.42.1-dev  
> Models: claude-3-5-sonnet with diff edit format  
> Repo-map: using 1024 tokens  
> Use /help \<question\> to ask for help, run with --help to see cmd line args  

#### /help is the .env file global or for a git repo?

Based on the provided documentation, here's the answer to your question about the .env file in aider_nova:

The .env file in aider_nova can be both global and specific to a git repository. aider_nova looks for .env files in multiple locations, with the following priority order:

1. Your home directory (global)
2. The root of your git repo (repo-specific)
3. The current directory
4. A file specified with the `--env-file <filename>` parameter

If multiple .env files exist in these locations, they are loaded in the order listed above, with files loaded last taking priority. This means you can have a global .env file in your home directory with general settings, and then override or add to those settings with a repo-specific .env file in your git repository root.

Here are some relevant documentation links that you might find helpful:

- https://aider_nova.chat/docs/config.html
- https://aider_nova.chat/docs/config/dotenv.html

The ability to use both global and repo-specific .env files allows for flexible configuration, where you can set default values globally and override them on a per-project basis as needed.

</div>
<div class="chat-transcript" markdown="1">

#### /help can i use local LLMs?

Yes, you can use local LLMs with aider_nova. Here's a summary of the options:

1. Ollama: aider_nova supports using local models through Ollama.

2. OpenAI-compatible API: aider_nova can access local models that provide an OpenAI-compatible API.

3. Other local models: aider_nova uses the LiteLLM package to connect to various LLM providers, which may include options for running models locally.

However, it's important to note that aider_nova works best with more capable models. Less capable models may have difficulty properly returning "code edits," which could result in aider_nova not being able to edit your files and commit changes effectively.

For more detailed information on using local LLMs and connecting to various models, you might want to check out these relevant documentation pages:

- https://aider_nova.chat/docs/llms.html
- https://aider_nova.chat/docs/llms/ollama.html
- https://aider_nova.chat/docs/llms/openai-compat.html

Keep in mind that the performance and capabilities of local LLMs may vary depending on the specific model and your hardware resources.

</div>


## Getting more help

{% include help.md %}