from libs.schema import BaseSchema, ListView
from datetime import datetime


class UserEdit(BaseSchema):
    email: str
    username: str
    password: str
    is_active: bool


class UserView(UserEdit):
    id: int


class UserRegisterView(BaseSchema):
    email: str
    username: str
    password: str
    password_repeat: str
    is_active: bool


class UserListView(ListView):
    items: list[UserView]

class UserCreateView(BaseSchema):
    pass
    # TODO: define me with hashed pwd
