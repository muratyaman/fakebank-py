# fakebank-py
Fakebank GraphQL server using Python, Starlette, SQLAlchemy, Psycopg and PostgreSQL

## installation

```
pip3 install uvicorn
pip3 install starlette
pip3 install graphene
pip3 install SQLAlchemy
pip3 install pyscopg2
```

## execution

```
uvicorn main:app
```

Open: http://127.0.0.1:8000/

Sample query:

```
query={users{username}}
```

Sample output:

```
{
    "data": {
        "users": [
            {
                "username": "john.smith"
            },
            {
                "username": "jane.smith"
            }
        ]
    }
}
```

## references

### Python

"Python is a programming language that lets you work quickly
and integrate systems more effectively."

[https://www.python.org/](https://www.python.org/)

### Starlette

"Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services."

[https://www.starlette.io/](https://www.starlette.io/)


### Uvicorn

"Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools."

[http://www.uvicorn.org/](http://www.uvicorn.org/)

### Graphene

"GraphQL framework for Python"

[https://github.com/graphql-python/graphene](https://github.com/graphql-python/graphene)

### SQLAlchemy

"The Database Toolkit for Python"

[https://github.com/sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)

### Pyscopg2

"PostgreSQL database adapter for the Python programming language"

[https://github.com/psycopg/psycopg2](https://github.com/psycopg/psycopg2)

