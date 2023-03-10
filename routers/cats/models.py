from sqlalchemy import Column, Integer, String

from libs.database import Base


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, index=True)
    age = Column(String)
    size = Column(String)
    gender = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "breed": self.breed,
            "age": self.age,
            "size": self.size,
            "gender": self.gender,
        }
