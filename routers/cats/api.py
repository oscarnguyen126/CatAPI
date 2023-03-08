from fastapi import APIRouter, Depends
from libs.database import get_db
from libs.crud import CRUD
from .schemas import CatEdit, CatListView, CatView
from .models import Cat

cat_router = APIRouter()


@cat_router.get("/", response_model=CatListView)
def read_cats(db=Depends(get_db), breed=None, offset=0, limit=100):
    crud = CRUD(model=Cat, db=db)
    if breed:
        crud.set_query(db.query(Cat).filter_by(breed=breed))
    return crud.paginate(limit=limit, offset=offset)


@cat_router.get("/{id}", response_model=CatView)
def read_cat(id: int, db=Depends(get_db)):
    return CRUD(model=Cat, db=db).get_by_id(id)


@cat_router.post("/", response_model=CatEdit)
def create_new_cat(cat: CatEdit, db=Depends(get_db)):
    return CRUD(model=Cat, db=db).create(cat)


@cat_router.put("/{id}", response_model=CatView)
def update_existing_cat(id: int, cat: CatEdit, db=Depends(get_db)):
    return CRUD(model=Cat, db=db).update(id, cat)


@cat_router.delete("/{id}")
def delete_existing_cat(id: int, db=Depends(get_db)):
    return CRUD(model=Cat, db=db).delete(id)
