from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import DogEdit, DogListView, DogView
from libs.database import get_db
from .models import Dog
from libs.crud import CRUD

dog_router = APIRouter()


@dog_router.get("/", response_model=DogListView)
def list_dog(db: Session = Depends(get_db), breed=None, offset=0, limit=None):
    crud = CRUD(model=Dog, db=db)
    if breed:
        crud.set_query(db.query(Dog).filter_by(breed=breed))
    return crud.paginate(limit=limit, offset=offset)


@dog_router.get("/{id}", response_model=DogView)
def get_dog(id: int, db=Depends(get_db)):
    return CRUD(model=Dog, db=db).get_by_id(id)


@dog_router.post("/", response_model=DogEdit)
def create_new_dog(payload: DogEdit, db=Depends(get_db)):
    return CRUD(db=db, model=Dog).create(payload)


@dog_router.put("/{id}", response_model=DogView)
def update_existing_dog(id: int, payload: DogEdit, db: Session = Depends(get_db)):
    return CRUD(model=Dog, db=db).update(id, payload)


@dog_router.delete("/{id}")
def delete_existing_dog(id: int, db: Session = Depends(get_db)):
    return CRUD(model=Dog, db=db).delete(id)
