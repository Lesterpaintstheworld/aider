---
parent: Troubleshooting
nav_order: 10
---

# File editing problems

Sometimes the LLM will reply with some code changes
that don't get applied to your local files.
In these cases, aider_nova might say something like "Failed to apply edit to *filename*"
or other error messages.

This usually happens because the LLM is disobeying the system prompts
and trying to make edits in a format that aider_nova doesn't expect.
aider_nova makes every effort to get the LLM
to conform, and works hard to deal with
LLMM edits that are "almost" correctly formatted.

But sometimes the LLM just won't cooperate.
In these cases, here are some things you might try.

## Use a capable model

If possible try using GPT-4o, Claude 3.5 Sonnet or Claude 3 Opus, 
as they are the strongest and most capable models.

Weaker models
are more prone to
disobeying the system prompt instructions.
Most local models are just barely capable of working with aider_nova,
so editing errors are probably unavoidable.

## Try the whole format

Run aider_nova with `--edit-format whole` if the model is using a different edit format.
You can see which edit format it is using in the announce lines:

```
aider_nova v0.50.2-dev
Models: claude-3-5-sonnet-20240620 with ♾️ diff edit format
```

## Reduce distractions

Many LLM now have very large context windows,
but filling them with irrelevant code or conversation 
can cofuse the model.

- Don't add too many files to the chat, *just* add the files you think need to be edited.
aider_nova also sends the LLM a [map of your entire git repo](https://aider_nova.chat/docs/repomap.html), so other relevant code will be included automatically.
- Use `/drop` to remove files from the chat session which aren't needed for the task at hand. This will reduce distractions and may help GPT produce properly formatted edits.
- Use `/clear` to remove the conversation history, again to help GPT focus.

## More help

{% include help.md %}
