#!/bin/bash

docker run \
       -it --rm \
       -v `pwd`:/aider_nova \
       -v `pwd`/tmp.benchmarks/.:/benchmarks \
       -e OPENAI_API_KEY=$OPENAI_API_KEY \
       -e HISTFILE=/aider_nova/.bash_history \
       -e aider_nova_DOCKER=1 \
       -e aider_nova_BENCHMARK_DIR=/benchmarks \
       aider_nova-benchmark \
       bash
