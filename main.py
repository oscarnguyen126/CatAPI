from typing import Union
from os import environ
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud, models, schemas
from database import get_db, engine
load_dotenv()


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worlddddd"}


@app.get("/cats", response_model=list[schemas.Cat])
def read_cats(db: Session = Depends(get_db)):
    cats = crud.get_all_cat(db)
    return cats


@app.get("/cats/{id}", response_model=schemas.Cat)
def read_cat(id:int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


@app.post("/cats", response_model=schemas.Cat)
def create_cat(cat: schemas.Cat, db: Session= Depends(get_db)):
    return crud.create_cat(db=db, cat=cat)


@app.put("/cats/{id}", response_model=schemas.Cat)
def update_cat(id:int, cat: schemas.Cat, db: Session= Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return crud.update_cat(db=db,  id=id, cat=cat)


@app.delete("/cats/{id}")
def delete_cat(id:int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat_by_id(db, id=id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return crud.delete_cat(db=db, id=id)
