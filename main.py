from fastapi import FastAPI


app = FastAPI()



@app.get('/blog')
def index(limit = 10, published: bool = True):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished pages'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)