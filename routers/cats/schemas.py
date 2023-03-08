from libs.schema import BaseSchema, ListView


class CatEdit(BaseSchema):
    breed: str
    size: str
    gender: str
    age: str


class CatView(CatEdit):
    id: str


class CatListView(ListView):
    items: list[CatView]
