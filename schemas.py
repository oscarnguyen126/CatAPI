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


class CatListView(BaseModel):
    total: int
    items: list[CatView]
    page: int
    pages: int

    class Config:
        orm_mode = True
