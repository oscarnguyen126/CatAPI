from sqlalchemy.orm import Session
from .models import Dog
from .schemas import DogEdit


def get_dog_by_id(db: Session, id: int):
    return db.query(Dog).filter(Dog.id == id).first()


def create_dog(db: Session, dog: DogEdit):
    db_dog = Dog(
        breed=dog.breed,
        origin=dog.origin,
        color=dog.origin,
        height=dog.height,
        eyes_color=dog.eyes_color,
        longevity=dog.longevity,
        character=dog.character,
        health_problems=dog.health_problems,
    )
    db.add(db_dog)
    db.commit()
    return db_dog


def update_dog(db: Session, id: int, dog: DogEdit):
    db_dog = db.query(Dog).filter(Dog.id == id).first()
    db_dog.breed = dog.breed
    db_dog.origin = dog.origin
    db_dog.color = dog.origin
    db_dog.height = dog.height
    db_dog.eyes_color = dog.eyes_color
    db_dog.longevity = dog.longevity
    db_dog.character = dog.character
    db_dog.health_problems = dog.health_problems
    db.commit()
    db.refresh(db_dog)
    return db_dog


def delete_dog(db: Session, id: int):
    db_dog = db.query(Dog).filter(Dog.id == id).first()
    db.delete(db_dog)
    db.commit()
    return f"The fcking dog has been slained"
