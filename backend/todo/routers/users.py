from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import users


router = APIRouter(
    prefix='/item',
    tags=['Users'],
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_users(id: int, db: Session = Depends(get_db)):
    return users.show_user(id, db)
