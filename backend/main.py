from fastapi import FastAPI

from backend.todo.routers import users, items
from backend.todo.database import engine
from backend.todo import models


app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

models.Base.metadata.create_all(bind=engine)
