from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models


def create_user(request: schemas.User, db: Session):
    new_user = models.User(name=request.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def show_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} not found")

    return user
