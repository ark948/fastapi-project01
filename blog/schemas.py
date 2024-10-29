from pydantic import BaseModel, ConfigDict
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    model_config = ConfigDict(orm_mode=True)


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    model_config = ConfigDict(orm_mode=True)


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    model_config = ConfigDict(orm_mode=True)



class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None