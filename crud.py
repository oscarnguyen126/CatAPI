from sqlalchemy.orm import Session

import models, schemas


def get_all_cat(db: Session):
    return db.query(models.Cat).offset(0).limit(100).all()


def get_cat_by_id(db: Session, id:int):
    return db.query(models.Cat).filter(models.Cat.id == id).first()

def create_cat(db: Session, cat: schemas.Cat):
    db_cat = models.Cat(breed=cat.breed, color=cat.color, age=cat.age, price=cat.price)
    db.add(db_cat)
    db.commit()
    return db_cat


def update_cat(db: Session, cat: schemas.Cat):
    pass
    # TODO: not implemented


def delete_cat(db: Session, id:int):
    db_cat = db.query(models.Cat).filter(models.Cat.id == id).first()
    db.delete(db_cat)
    db.commit()
    return f"This cat has been slained"














# from sqlalchemy.orm import Session

# from . import models, schemas



# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

