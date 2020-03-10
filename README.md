# Dicas e Truqes MongoDB

[Download do Robo3T](https://robomongo.org/download)

# exercicio

- tenham um banco rodando na sua máquina (vocês podem usar um comando do docker por exemplo)
- rodem o arquivo para iniciar os registros: `python app/start_db.py`

Vocês vão precisar mexer só no arquivo `app/app.py`

O objetivo é converter as queries da função `get` da API para pymongo


# pymongo

é o pacote básico para conectar com o MongoDB usando python

ele tem praticamente a mesma sintaxe de como se você estivesse usando o mongo pelo terminal

`pip install pymongo`

https://api.mongodb.com/python/current/


# mongoengine

uma ORM para te ajudar a definir os modelos e conexões do seu projeto, e também para tratar os fields (campos obrigatório, conversão de valores, etc)


`pip install mongoengine`

`pip install flask_mongoengine`

http://docs.mongoengine.org/index.html