from sqlalchemy import Column, Integer, String, DateTime, Boolean
from libs.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    password_repeat = Column(String)
    create_at = Column(DateTime)
    is_active = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "password_repeat": self.password_repeat,
            "create_at": self.create_at,
            "is_active": self.is_active,
        }
