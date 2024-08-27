---
parent: Usage
nav_order: 25
description: Tips for AI pair programming with aider_nova.
---

# Tips

- Think about which files need to be edited to make your change and add them to the chat.
aider_nova can help the LLM figure out which files to edit all by itself, but the most efficient approach is to add the needed files to the chat yourself.
- Don't add *everything* to the chat, just the files you think need to be edited.
aider_nova also sends the LLM a [map of your entire git repo](https://aider_nova.chat/docs/repomap.html).
So the LLM can see all the other relevant parts of your code base.
- Large changes are best performed as a sequence of thoughtful bite sized steps, where you plan out the approach and overall design. Walk the LLM through changes like you might with a junior dev. Ask for a refactor to prepare, then ask for the actual change. Spend the time to ask for code quality/structure improvements.
- It's always safe to use Control-C to interrupt aider_nova if it isn't providing a useful response. The partial response remains in the conversation, so you can refer to it when you reply to the LLM with more information or direction.
- If your code is throwing an error, 
use the `/run` [in-chat command](/docs/usage/commands.html)
to share the error output with the aider_nova.
Or just paste the errors into the chat. Let the aider_nova figure out and fix the bug.
- If test are failing, use the `/test` [in-chat command](/docs/usage/commands.html)
to run tests and
share the error output with the aider_nova.
- {% include multi-line.md %}
- LLMs know about a lot of standard tools and libraries, but may get some of the fine details wrong about API versions and function arguments.
You can paste doc snippets into the chat to resolve these issues.

