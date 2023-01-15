from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    todo_items = relationship('TodoList', back_populates='owner')


class TodoList(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship('User', back_populates='todo_items')
