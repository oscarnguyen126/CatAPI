from pydantic import BaseModel, Field

class Cat(BaseModel):
    id: int # TODO: do not enforce submit ID on create
    breed: str
    color: str
    age: int
    price: float = Field(gt=0, description="The price must be greater than zero")

    class Config:
        orm_mode = True