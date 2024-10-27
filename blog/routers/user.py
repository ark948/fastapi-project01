from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
import database, schemas, models
from sqlalchemy.orm import Session
from hashing import Hash


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} was not found.")
    return user