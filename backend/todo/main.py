from fastapi import FastAPI

from .routers import users, items
from .database import engine
from . import models


app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

models.Base.metadata.create_all(bind=engine)
