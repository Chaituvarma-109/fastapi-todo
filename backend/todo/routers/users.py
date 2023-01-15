from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import users

router = APIRouter(
    prefix='/item',
    tags=['Users'],
)


# response_model=schemas.ShowUser
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_users(id: int, db: Session = Depends(get_db)):
    return users.show_user(id, db)
