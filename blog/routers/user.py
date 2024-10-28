from fastapi import APIRouter, Depends, HTTPException, status
import database, schemas
from sqlalchemy.orm import Session
from crud import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)