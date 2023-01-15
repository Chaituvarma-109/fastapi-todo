from pydantic import BaseModel


class TodoListBase(BaseModel):
    description: str


class TodoList(TodoListBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str


class ShowUser(BaseModel):
    name: str
    item: list[TodoList] = []

    class Config:
        orm_mode = True


class ShowList(BaseModel):
    description: str
    creator: ShowUser

    class Config:
        orm_mode = True
