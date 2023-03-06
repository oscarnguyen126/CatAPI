from pydantic import BaseModel, Field

class Cat(BaseModel):
    breed: str
    size: str
    gender: str
    age: str

    class Config:
        orm_mode = True