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


### TODO

```
1. Refactor dogs api:
    - remove crud.py
    - replace crud operations by libs/crud
    - inherit ListView

2. 
```
