---
parent: Installation
nav_order: 20
---

# Optional steps
{: .no_toc }

The steps below are completely optional.

- TOC
{:toc}


## Store your api keys 

You can [store your api keys in a .env file](/docs/config/dotenv.html)
and they will be loaded automatically whenever you run aider_nova.

## Enable Playwright 

aider_nova supports adding web pages to the chat with the `/web <url>` command.
When you add a url to the chat, aider_nova fetches the page and scrapes its
content.

By default, aider_nova uses the `httpx` library to scrape web pages, but this only
works on a subset of web pages.
Some sites explicitly block requests from tools like httpx.
Others rely heavily on javascript to render the page content,
which isn't possible using only httpx.

aider_nova works best with all web pages if you install
Playwright's chromium browser and its dependencies:

```
playwright install --with-deps chromium
```

See the
[Playwright for Python documentation](https://playwright.dev/python/docs/browsers#install-system-dependencies)
for additional information.


## Enable voice coding 

aider_nova supports 
[coding with your voice](https://aider_nova.chat/docs/usage/voice.html)
using the in-chat `/voice` command.
aider_nova uses the [PortAudio](http://www.portaudio.com) library to
capture audio.
Installing PortAudio is completely optional, but can usually be accomplished like this:

- For Windows, there is no need to install PortAudio.
- For Mac, do `brew install portaudio`
- For Linux, do `sudo apt-get install libportaudio2`

## Add aider_nova to your editor 

Other projects have integrated aider_nova into some IDE/editors.
It's not clear if they are tracking the latest
versions of aider_nova,
so it may be best to just run the latest
aider_nova in a terminal alongside your editor.

### NeoVim

[joshuavial](https://github.com/joshuavial) provided a NeoVim plugin for aider_nova:

[https://github.com/joshuavial/aider_nova.nvim](https://github.com/joshuavial/aider_nova.nvim)

### VS Code

joshuavial also confirmed that aider_nova works inside a VS Code terminal window.
aider_nova detects if it is running inside VSCode and turns off pretty/color output,
since the VSCode terminal doesn't seem to support it well.

[MattFlower](https://github.com/MattFlower) provided a VSCode plugin for aider_nova:

[https://marketplace.visualstudio.com/items?itemName=MattFlower.aider_nova](https://marketplace.visualstudio.com/items?itemName=MattFlower.aider_nova)

### Other editors

If you are interested in creating an aider_nova plugin for your favorite editor,
please let me know by opening a
[GitHub issue](https://github.com/paul-gauthier/aider_nova/issues).


## Install the development version of aider_nova 

If you want the very latest development version of aider_nova
you can install directly from GitHub:

```
python -m pip install --upgrade git+https://github.com/paul-gauthier/aider_nova.git
```

If you've git cloned the aider_nova repository already, you can install "live" from your local copy. This is mostly useful if you are developing aider_nova and want your current modifications to take effect immediately.

```
python -m pip install -e .
```

