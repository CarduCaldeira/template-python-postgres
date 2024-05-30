FROM python:3.11.4-bullseye as install-poetry

# Python version must be 3.5 or higher
# Poetry version must be 1.1.7 or higher
RUN curl -sSL https://install.python-poetry.org > ./install-poetry.py

FROM python:3.11.4-slim-bullseye

ENV POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_HOME=/usr/bin/poetry \
    PATH=/usr/bin/poetry/bin:$PATH
    
# Python version must be 3.5 or higher
# Poetry must version be 1.1.7 or higher
COPY --from=install-poetry ./install-poetry.py ./
RUN python ./install-poetry.py \
    && rm ./install-poetry.py

ARG USER_NAME=myuser
ARG WORK_DIR=/home/$USER_NAME/PROJECT
ARG GROUP_ID=1000
ARG USER_ID=1000

RUN apt-get update && apt-get install --yes --no-install-recommends git=1:2.30.* \
    && rm -rf /var/lib/apt/lists/* 
    
RUN groupadd --gid $GROUP_ID grupo_user \
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME \
    && mkdir --parents $WORK_DIR  \
    && chown -R $USER_NAME:grupo_user /home/$USER_NAME

USER $USER_NAME
WORKDIR $WORK_DIR