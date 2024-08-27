---
parent: More info
nav_order: 900
description: aider_nova supports pretty much all popular coding languages.
---
# Supported languages

aider_nova should work well with most popular coding languages.
This is because top LLMs are fluent in most mainstream languages,
and familiar with popular libraries, packages and frameworks.

aider_nova has specific support for linting many languages.
By default, aider_nova runs the built in linter any time a file is edited.
If it finds syntax errors, aider_nova will offer to fix them for you.
This helps catch small code issues and quickly fix them.

aider_nova also does code analysis to help
the LLM navigate larger code bases by producing
a [repository map](https://aider_nova.chat/docs/repomap.html).
aider_nova can currently produce repository maps for many popular
mainstream languages, listed below.


<!--[[[cog
from aider_nova.repomap import get_supported_languages_md
cog.out(get_supported_languages_md())
]]]-->

| Language | File extension | Repo map | Linter |
|:--------:|:--------------:|:--------:|:------:|
| bash                 | .bash                |          |   ✓    |
| c                    | .c                   |    ✓     |   ✓    |
| c_sharp              | .cs                  |    ✓     |   ✓    |
| commonlisp           | .cl                  |          |   ✓    |
| cpp                  | .cc                  |    ✓     |   ✓    |
| cpp                  | .cpp                 |    ✓     |   ✓    |
| css                  | .css                 |          |   ✓    |
| dockerfile           | .dockerfile          |          |   ✓    |
| dot                  | .dot                 |          |   ✓    |
| elisp                | .el                  |    ✓     |   ✓    |
| elixir               | .ex                  |    ✓     |   ✓    |
| elm                  | .elm                 |    ✓     |   ✓    |
| embedded_template    | .et                  |          |   ✓    |
| erlang               | .erl                 |          |   ✓    |
| go                   | .go                  |    ✓     |   ✓    |
| gomod                | .gomod               |          |   ✓    |
| hack                 | .hack                |          |   ✓    |
| haskell              | .hs                  |          |   ✓    |
| hcl                  | .hcl                 |          |   ✓    |
| html                 | .html                |          |   ✓    |
| java                 | .java                |    ✓     |   ✓    |
| javascript           | .js                  |    ✓     |   ✓    |
| javascript           | .mjs                 |    ✓     |   ✓    |
| jsdoc                | .jsdoc               |          |   ✓    |
| json                 | .json                |          |   ✓    |
| julia                | .jl                  |          |   ✓    |
| kotlin               | .kt                  |          |   ✓    |
| lua                  | .lua                 |          |   ✓    |
| make                 | .mk                  |          |   ✓    |
| objc                 | .m                   |          |   ✓    |
| ocaml                | .ml                  |    ✓     |   ✓    |
| perl                 | .pl                  |          |   ✓    |
| php                  | .php                 |    ✓     |   ✓    |
| python               | .py                  |    ✓     |   ✓    |
| ql                   | .ql                  |    ✓     |   ✓    |
| r                    | .R                   |          |   ✓    |
| r                    | .r                   |          |   ✓    |
| regex                | .regex               |          |   ✓    |
| rst                  | .rst                 |          |   ✓    |
| ruby                 | .rb                  |    ✓     |   ✓    |
| rust                 | .rs                  |    ✓     |   ✓    |
| scala                | .scala               |          |   ✓    |
| sql                  | .sql                 |          |   ✓    |
| sqlite               | .sqlite              |          |   ✓    |
| toml                 | .toml                |          |   ✓    |
| tsq                  | .tsq                 |          |   ✓    |
| typescript           | .ts                  |    ✓     |   ✓    |
| typescript           | .tsx                 |    ✓     |   ✓    |
| yaml                 | .yaml                |          |   ✓    |

<!--[[[end]]]-->



## How to add support for another language

aider_nova should work quite well for other languages, even those
without repo map or linter support.
You should really try coding with aider_nova before
assuming it needs better support for your language.

That said, if aider_nova already has support for linting your language,
then it should be possible to add repo map support.
To build a repo map, aider_nova needs the `tags.scm` file
from the given language's tree-sitter grammar.
If you can find and share that file in a 
[GitHub issue](https://github.com/paul-gauthier/aider_nova/issues),
then it may be possible to add repo map support.

If aider_nova doesn't support linting, it will be complicated to
add linting and repo map support.
That is because aider_nova relies on 
[py-tree-sitter-languages](https://github.com/grantjenks/py-tree-sitter-languages)
to provide pre-packaged versions of tree-sitter
parsers for many languages.

aider_nova needs to be easy for users to install in many environments,
and it is probably too complex to add dependencies on
additional individual tree-sitter parsers.
