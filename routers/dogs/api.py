from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import DogEdit, DogListView, DogView
import math
from routers.dogs.crud import create_dog, get_dog_by_id, delete_dog, update_dog
from libs.database import get_db
from .models import Dog


dog_router = APIRouter()


@dog_router.get("/", response_model=DogListView)
def list_dog(db: Session = Depends(get_db), breed=None, offset=0, limit=None):
    query = db.query(Dog).filter_by(breed=breed) if breed else db.query(Dog)
    dog_counter = query.count()
    dogs = query.offset(offset).limit(limit or dog_counter).all()

    page = math.ceil(int(offset) / int(limit)) if limit and offset else 1
    pages = math.ceil(dog_counter / int(limit)) if limit else 1

    return {
        "items": [d.to_dict() for d in dogs],
        "total": len(dogs),
        "page": page,
        "pages": pages,
    }


@dog_router.get("/{id}", response_model=DogView)
def get_dog(id: int, db: Session = Depends(get_db)):
    db_dog = get_dog_by_id(db, id=id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_dog


@dog_router.post("/", response_model=DogEdit)
def create_new_dog(dog: DogEdit, db: Session = Depends(get_db)):
    return create_dog(db=db, dog=dog)


@dog_router.put("/{id}", response_model=DogView)
def update_existing_dog(id: int, dog: DogEdit, db: Session = Depends(get_db)):
    db_dog = get_dog_by_id(db, id=id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return update_dog(db=db, id=id, dog=dog)


@dog_router.delete("/{id}")
def delete_existing_dog(id: int, db: Session = Depends(get_db)):
    db_dog = get_dog_by_id(db, id=id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not fount")
    return delete_dog(db=db, id=id)
