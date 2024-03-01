FROM python:3.10.12-bullseye as install-poetry

# Python version must be 3.5 or higher
# Poetry version must be 1.1.7 or higher
RUN curl -sSL https://install.python-poetry.org > ./install-poetry.py

FROM ubuntu:22.04

RUN apt update &&  apt install -y wget build-essential  zlib1g-dev \ 
        libncurses5-dev libgdbm-dev libnss3-dev libssl-dev \
        libreadline-dev libffi-dev libsqlite3-dev libbz2-dev libpq-dev gcc\
        liblzma-dev && \
        apt clean && \
        rm -rf /var/lib/apt/lists/*

RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz && \
    tar -xvf Python-3.10.12.tgz && \
    cd Python-3.10.12 && \
    ./configure --enable-optimizations && \
    make && make install && \
    cd .. && rm Python-3.10.12.tgz && rm -r Python-3.10.12 && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python 

ENV POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_HOME=/usr/bin/poetry \
    PATH=/usr/bin/poetry/bin:$PATH
    
# Python version must be 3.5 or higher
# Poetry must version be 1.1.7 or higher
COPY --from=install-poetry ./install-poetry.py ./
RUN python ./install-poetry.py \
    && rm ./install-poetry.py

ARG GROUP_ID=1000
ARG USER_ID=1000
ARG USER_NAME=myuser
ARG WORK_DIR=/home/$USER_NAME/PROJECT

RUN groupadd --gid $GROUP_ID $USER_NAME \
    && useradd --uid $USER_ID --gid $GROUP_ID --create-home $USER_NAME \
    && runuser --user $USER_NAME -- mkdir  $WORK_DIR 

RUN runuser --user $USER_NAME -- chown -R $USER_NAME:$USER_NAME $WORK_DIR

USER $USER_NAME
WORKDIR $WORK_DIR
