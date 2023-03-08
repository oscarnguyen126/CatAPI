# FastApi Demo

## Prepare development environment

Activate virtual env

```
source env/bin/activate
```

Install dependencies

```
pipenv install
```

Fill in .env after populating .env file

```
cp .env.example .env
```

Run server

```
uvicorn main:app --reload
```


Apply changes from models to database:

``` 
alembic revision --autogenerate -m <your commit message>

alembic upgrade head
```


### new project structure

```
/catapi
    /routers
        /cats
            models.py
            crud.py
            api.py
        /dogs
            models.py
            crud.py
            api.py
    /libs
        /migrations
        alembic.ini
        database.py
        seed.py
    .env
    .env.example
    .gitignore
    Makefile
    README.md
    Pipfile
    Pipfile.lock
    main.py
```
