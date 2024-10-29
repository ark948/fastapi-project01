from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from blog.models import Base
from blog.database import engine
from blog.routers import auth, blog, user, pages


app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(pages.router)
app.include_router(blog.router)
app.include_router(user.router)


app.mount('/static', StaticFiles(directory='static'), name='static')