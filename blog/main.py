from fastapi import FastAPI
import models
from database import engine
from routers import blog, user, auth


app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)