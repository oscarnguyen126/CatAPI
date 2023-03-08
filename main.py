from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import FastAPI
from libs.database import Base, engine
from routers.cats.api import cat_router
from routers.dogs.api import dog_router

load_dotenv()


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(cat_router, prefix="/cats")
app.include_router(dog_router, prefix="/dogs")
