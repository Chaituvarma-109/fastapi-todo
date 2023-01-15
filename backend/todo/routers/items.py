from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import items


router = APIRouter(
    prefix='/user',
    tags=['Items'],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_item(request: schemas.TodoList, db: Session = Depends(get_db)):
    return items.create_item(request, db)
