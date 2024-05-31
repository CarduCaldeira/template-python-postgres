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

## DOCKER

Para executar o container
```
docker compose -f docker/docker-compose.yml up -d
docker compose -f  docker/docker-compose.yml exec python-project bash 
```  
Ou rode o script
```
./start.sh
```

## MKDCOS

Para gerar a documentação com o mkdocs de o comando
```
mkdocs serve -a 0.0.0.0:8000 > mkdocs.log 2>&1
```
Para redirecionar a saída para um arquivo de log
```
mkdocs serve -a 0.0.0.0:8000 > mkdocs.log 2>&1
```
Para gerar a documentação automatica baseada nas docstrings, insira em docs/source um arquivo <name>.md, por exemplo insira db.md com o conteudo
```
:::db
```
Isso automantiacamente gerara uma documentação com as docstrings do modulo source/db.py 

## PYTEST e BANDIT

No modulo tests/conftest.py são definidas as fixtures (funções de inicialização e encerramento de contexto para os testes). Como exemplo é testado a conexão com o banco de dados. O script test_app.py é adicionado como exemplo de uso do parametrize.

Para  rodar o bandit
```
bandit -r .
```

## IPYTHON
 
Para o uso interativo para desenvolvimento adicionei o ipython, para importar as funções de um script rode por exemplo:
```
poetry run ipython -i source/db.py
```
Voce pode então rodar as funções diretamente como por exemplo:
```
create_database_connection()
```

## TASKIPY 
Para simplificar alguns comandos foi instalado o taskipy, para os comandos definidos basta dar task <comando>, por exemplo:
```
task test
```

## RUFF
Ruff é um linter e formatador, para checar o linter:
```
ruff check .
```
Para formatar:
```
ruff check . --fix
```
