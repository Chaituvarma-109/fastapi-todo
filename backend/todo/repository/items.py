from sqlalchemy.orm import Session

from .. import schemas, models


def create_item(request: schemas.TodoList, db: Session):
    new_item = models.TodoList(description=request.description, user_id=1)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def get_all_items(db: Session):
    todo_items = db.query(models.TodoList).all()
    return todo_items
