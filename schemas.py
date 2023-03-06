from pydantic import BaseModel, Field


class CatEdit(BaseModel):
    breed: str
    size: str
    gender: str
    age: str

    class Config:
        orm_mode = True


class CatView(CatEdit):
    id: str
