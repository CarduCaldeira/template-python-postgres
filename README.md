Este repositorio tem como objetivo criar um ambiente de desenvolvimento em python, postgres, poetry, testes, formatadores e documentação em um container. 

Ao subir o postgres, o script data/start.sql sera executado (so é executado a primeira vez que o container é executado, aleḿ disso, se ja existir o database em que o script realiza as queries, o script é ignorado). 

No arquivo docker/.env é inicializado os parametros necessarios pra
construçao do container. Por exemplo

```
DB_NAME="raw_data"
DB_USER="user-name"
DB_PASSWORD="strong-password"
DB_HOST="db"
DB_PORT="5432"
```

Para executar 
```
docker compose -f docker/docker-compose.yml up
docker compose -f  docker/docker-compose.yml python-project bash 
```
