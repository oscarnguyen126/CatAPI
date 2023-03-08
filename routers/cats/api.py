from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import CatEdit, CatListView, CatView
import math
from routers.cats.crud import create_cat, delete_cat, get_cat_by_id
from .models import Cat
from libs.database import get_db

cat_router = APIRouter()


@cat_router.get("/", response_model=CatListView)
def read_cats(db: Session = Depends(get_db), breed=None, offset=0, limit=100):
    query = db.query(Cat).filter_by(breed=breed) if breed else db.query(Cat)
    cat_count = query.count()
    cats = query.offset(offset).limit(limit or cat_count).all()

    page = math.ceil(int(offset) / int(limit)) if limit and offset else 1
    pages = math.ceil(cat_count / int(limit)) if limit else 1

    return {
        "items": [c.to_dict() for c in cats],
        "total": len(cats),
        "page": page,
        "pages": pages,
    }


@cat_router.get("/{id}", response_model=CatView)
def read_cat(id: int, db: Session = Depends(get_db)):
    db_cat = get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


@cat_router.post("/", response_model=CatEdit)
def create_new_cat(cat: CatEdit, db: Session = Depends(get_db)):
    return create_cat(db=db, cat=cat)


@cat_router.put("/{id}", response_model=CatView)
def update_existing_cat(id: int, cat: CatEdit, db: Session = Depends(get_db)):
    db_cat = get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return update_cat(db=db, id=id, cat=cat)


@cat_router.delete("/{id}")
def delete_existing_cat(id: int, db: Session = Depends(get_db)):
    db_cat = get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return delete_cat(db=db, id=id)
