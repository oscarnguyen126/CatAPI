from fastapi import APIRouter

dog_router = APIRouter()


@dog_router.get("/sua")
def index():
    return {"msg": "woff"}
