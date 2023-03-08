from sqlalchemy import Column, Integer, String
from libs.database import Base


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String)
    origin = Column(String)
    color = Column(String)
    height = Column(String)
    eyes_color = Column(String)
    longevity = Column(String)
    character = Column(String)
    health_problems = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "breed": self.breed,
            "origin": self.origin,
            "color": self.color,
            "height": self.height,
            "eyes_color": self.eyes_color,
            "longevity": self.longevity,
            "character": self.character,
            "health_problems": self.health_problems,
        }
