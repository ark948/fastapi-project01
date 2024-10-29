from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
from blog.crud import blog
from blog import database, schemas
from blog.oauth2 import get_current_user


router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


# IMPORTANT notice schema is used for validation and models for actual creation of data
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)