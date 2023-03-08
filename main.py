from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Cat
from math import ceil
import crud, models, schemas
from database import get_db, engine

load_dotenv()


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Worlddddd"}


@app.get("/cats", response_model=schemas.CatListView)
def read_cats(db: Session = Depends(get_db), breed=None, offset=None, limit=None):
    query = db.query(Cat).filter_by(breed=breed) if breed else db.query(Cat)
    cat_count = query.count()
    cats = query.offset(offset or 0).limit(limit or cat_count).all()

    page = ceil(int(offset) / int(limit)) if limit else 1
    pages = ceil(cat_count / int(limit)) if limit else 1

    return {
        "items": [c.to_dict() for c in cats],
        "total": len(cats),
        "page": page,
        "pages": pages,
    }


@app.get("/cats/{id}", response_model=schemas.CatView)
def read_cat(id: int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


@app.post("/cats", response_model=schemas.CatEdit)
def create_cat(cat: schemas.CatEdit, db: Session = Depends(get_db)):
    return crud.create_cat(db=db, cat=cat)


@app.put("/cats/{id}", response_model=schemas.CatView)
def update_cat(id: int, cat: schemas.CatEdit, db: Session = Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return crud.update_cat(db=db, id=id, cat=cat)


@app.delete("/cats/{id}")
def delete_cat(id: int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return crud.delete_cat(db=db, id=id)
