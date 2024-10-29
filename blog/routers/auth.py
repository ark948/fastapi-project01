from fastapi import APIRouter, Depends, HTTPException, status
from blog.tokens import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog.database import get_db
from blog import models
from blog.hashing import Hash


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials.")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password.")
    
    access_token = create_access_token(data={"sub": user.email})
    # return Token(access_token=access_token, token_type="bearer")
    return {'access_token': access_token, "token_type": "bearer"}