from sqlalchemy import Column, Integer, String

from database import Base

class Cat(Base):
    __tablename__ = "Cat"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, index=True)
    age = Column(String)
    size = Column(String)
    gender = Column(String)
