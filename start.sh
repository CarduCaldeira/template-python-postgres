#!/bin/bash

# Verifica se o diretório ../ignorefolder existe, e se não, cria ele
if [ ! -d "./ignorefolder" ]; then
  echo "Directory ./ignorefolder does not exist. Creating..."
  mkdir -p ./ignorefolder
else
  echo "Directory ./ignorefolder already exists."
fi

# Inicia o Docker Compose
docker compose -f docker/docker-compose.yml up -d
docker compose -f  docker/docker-compose.yml exec python-project bash 