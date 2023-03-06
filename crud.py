from sqlalchemy.orm import Session

import models, schemas


def get_all_cat(db: Session):
    return db.query(models.Cat).offset(0).limit(100).all()


def get_cat_by_id(db: Session, id: int):
    return db.query(models.Cat).filter(models.Cat.id == id).first()


def create_cat(db: Session, cat: schemas.Cat):
    db_cat = models.Cat(breed=cat.breed, size=cat.size, age=cat.age, gender=cat.gender)
    db.add(db_cat)
    db.commit()
    return db_cat


def update_cat(db: Session, id: int, cat: schemas.Cat):
    db_cat = db.query(models.Cat).filter(models.Cat.id == id).first()
    db_cat.breed = cat.breed
    db_cat.size = cat.size
    db_cat.gender = cat.gender
    db_cat.age = cat.age
    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, id: int):
    db_cat = db.query(models.Cat).filter(models.Cat.id == id).first()
    db.delete(db_cat)
    db.commit()
    return f"This cat has been slained"
