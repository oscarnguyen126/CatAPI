from fastapi import APIRouter, Depends, HTTPException
from libs.database import get_db
from libs.crud import CRUD
import re
from .models import User
from .schemas import UserEdit, UserView, UserRegisterView, UserListView
import bcrypt


user_router = APIRouter()

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def validate_email(email):
    return re.fullmatch(regex, email)

def hash_password(password):
    password = b'password'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed

@user_router.post("/create_user", response_model=UserRegisterView)
def register(payload: UserRegisterView, db=Depends(get_db)):
    if not validate_email(payload.email):
        raise HTTPException(
            status_code=400,
            detail=f"email is not valid",
        )
    # import pdb; pdb.set_trace()
    crud = CRUD(model=User, db=db)
    persisted_user = crud.find({"email": payload.email})
    if persisted_user:
        raise HTTPException(
            status_code=400,
            detail=f"user is already exist",
        )

    if payload.password != payload.password_repeat:
        raise HTTPException(
            status_code=400,
            detail=f"The password repeat is not the same as the password",
        )
    
    payload.password = hash_password(password=payload.password)
    payload.password = hash_password(password=payload.password_repeat)
    return crud.create(payload)


    # TODO:
    # 1. check password valid
    # 2. hash password
    # 3. create UserCreateView
    crud.create(payload)
    return user

@user_router.get("/", response_model=UserListView)
def get_users(db=Depends(get_db), offset=0, limit=100):
    crud = CRUD(model=User, db=db)
    return crud.paginate(limit=limit, offset=offset)


@user_router.get("/{id}", response_model=UserView)
def get_user_by_id(id: int, db=Depends(get_db)):
    return CRUD(model=User, db=db).get_by_id(id)
