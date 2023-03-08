from pydantic import BaseModel


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True


class ListView(BaseSchema):
    total: int
    items: list[None]
    page: int
    pages: int
