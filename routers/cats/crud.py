from sqlalchemy.orm import Session
from .models import Cat
from .schemas import CatEdit


def get_all_cat(db: Session):
    return db.query(Cat).offset(0).limit(100).all()


def get_cat_by_id(db: Session, id: int):
    return db.query(Cat).filter(Cat.id == id).first()


def create_cat(db: Session, cat: CatEdit):
    db_cat = Cat(breed=cat.breed, size=cat.size, age=cat.age, gender=cat.gender)
    db.add(db_cat)
    db.commit()
    return db_cat


def update_cat(db: Session, id: int, cat: CatEdit):
    db_cat = db.query(Cat).filter(Cat.id == id).first()
    db_cat.breed = cat.breed
    db_cat.size = cat.size
    db_cat.gender = cat.gender
    db_cat.age = cat.age
    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, id: int):
    db_cat = db.query(Cat).filter(Cat.id == id).first()
    db.delete(db_cat)
    db.commit()
    return f"This cat has been slained"
