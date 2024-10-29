from fastapi import FastAPI
from blog.models import Base
from blog.database import engine
from blog.routers import auth, blog, user


app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)