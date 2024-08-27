FROM python:3.10-slim AS base

RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential git libportaudio2 pandoc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# https://playwright.dev/python/docs/browsers
ENV PLAYWRIGHT_BROWSERS_PATH=/pw-browsers
ENV PLAYWRIGHT_SKIP_BROWSER_GC=1

# Permission kludges to support `docker run --user xxx`
RUN chmod a+rwx /venv /venv/bin /venv/include /venv/lib /venv/lib/python3.10/site-packages

RUN mkdir       /.aider_nova /.cache /pw-browsers
RUN chmod a+rwx /.aider_nova /.cache /pw-browsers

# So git doesn't complain about unusual permissions
RUN git config --system --add safe.directory /app

#########################
FROM base AS aider_nova-full

ENV aider_nova_DOCKER_IMAGE=paulgauthier/aider_nova-full

COPY . /tmp/aider_nova
RUN /venv/bin/python -m pip install --upgrade --no-cache-dir pip \
    && /venv/bin/python -m pip install --no-cache-dir /tmp/aider_nova[help,browser,playwright] \
       --extra-index-url https://download.pytorch.org/whl/cpu \
    && rm -rf /tmp/aider_nova

RUN /venv/bin/python -m playwright install --with-deps chromium
RUN find /venv/lib/python3.10/site-packages \( -type d -exec chmod a+rwx {} + \) -o \( -type f -exec chmod a+rw {} + \)

ENTRYPOINT ["/venv/bin/aider_nova"]

#########################
FROM base AS aider_nova

ENV aider_nova_DOCKER_IMAGE=paulgauthier/aider_nova

COPY . /tmp/aider_nova
RUN /venv/bin/python -m pip install --upgrade --no-cache-dir pip \
    && /venv/bin/python -m pip install --no-cache-dir /tmp/aider_nova[playwright] \
       --extra-index-url https://download.pytorch.org/whl/cpu \
    && rm -rf /tmp/aider_nova

RUN /venv/bin/python -m playwright install --with-deps chromium
RUN find /venv/lib/python3.10/site-packages \( -type d -exec chmod a+rwx {} + \) -o \( -type f -exec chmod a+rw {} + \)

ENTRYPOINT ["/venv/bin/aider_nova"]
