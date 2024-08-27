---
parent: Example chat transcripts
---
# Semantic search & replace code with aider_nova

In this chat transcript, the user asks to modify a series of function calls. 

Notice that it isn't replacing exact strings.
Making the change requires dealing with various formatting and semantic differences in the calls that it is updating.

Some edits were elided from this transcript for brevity.

<div class="chat-transcript" markdown="1">

> $ aider_nova aider_nova/coder.py  
> Added aider_nova/coder.py to the chat  

#### replace all the self.console.print() calls that contain [red] with calls to self.io.tool_error() with [red] removed from the string

```python
aider_nova/coder.py
<<<<<<< ORIGINAL
            self.console.print(
                f"[red]This tool will almost certainly fail to work with {main_model}"
            )
=======
            self.io.tool_error(f"This tool will almost certainly fail to work with {main_model}")
>>>>>>> UPDATED
```

```python
aider_nova/coder.py
<<<<<<< ORIGINAL
            self.console.print("[red]Files are not in a git repo.")
=======
            self.io.tool_error("Files are not in a git repo.")
>>>>>>> UPDATED
```

```python
aider_nova/coder.py
<<<<<<< ORIGINAL
            self.console.print("[red]Malformed ORIGINAL/UPDATE blocks, retrying...")
            self.console.print("[red]", Text(err))
=======
            self.io.tool_error("Malformed ORIGINAL/UPDATE blocks, retrying...")
            self.io.tool_error(Text(err))
>>>>>>> UPDATED
```

Please note that I couldn't find the `self.io.tool_error()` method in the provided code. You may need to create this method in the appropriate class or provide the correct method name to replace the `self.console.print()` calls.

> Applied edit to aider_nova/coder.py  
> Applied edit to aider_nova/coder.py  
> Applied edit to aider_nova/coder.py  
> Commit 919cfc2 aider_nova: Replaced all self.console.print() calls with self.io.tool_error() calls with [red] removed from the string.  


</div>
