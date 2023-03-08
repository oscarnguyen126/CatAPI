from libs.schema import BaseSchema


class DogEdit(BaseSchema):
    breed: str
    origin: str
    color: str
    height: str
    eyes_color: str
    longevity: str
    character: str
    health_problems: str


class DogView(DogEdit):
    id: int


class DogListView(BaseSchema):
    total: int
    items: list[DogView]
    page: int
    pages: int
