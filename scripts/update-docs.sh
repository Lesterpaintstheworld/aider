#!/bin/bash

# exit when any command fails
set -e

if [ -z "$1" ]; then
  ARG=-r
else
  ARG=$1
fi

# README.md before index.md, because index.md uses cog to include README.md
cog $ARG \
    README.md \
    aider_nova/website/index.md \
    aider_nova/website/HISTORY.md \
    aider_nova/website/docs/usage/commands.md \
    aider_nova/website/docs/languages.md \
    aider_nova/website/docs/config/dotenv.md \
    aider_nova/website/docs/config/options.md \
    aider_nova/website/docs/config/aider_nova_conf.md \
    aider_nova/website/docs/leaderboards/index.md \
    aider_nova/website/docs/llms/other.md
