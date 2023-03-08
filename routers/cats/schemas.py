from libs.schema import BaseSchema


class CatEdit(BaseSchema):
    breed: str
    size: str
    gender: str
    age: str


class CatView(CatEdit):
    id: str


class CatListView(BaseSchema):
    total: int
    items: list[CatView]
    page: int
    pages: int
