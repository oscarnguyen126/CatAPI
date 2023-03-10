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

2. Create users api:
    an user has:
        - id
        - email
        - username
        - password (hashed: https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/)
        - created_at
        - is_active
    api:
    - create user: register user
        params: email, username, password, password-repeat, is_active=false
    - update user:
        can only update username, password
    - activate_user:
        pending
    - delete user: by id
```
hi