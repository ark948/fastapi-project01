from fastapi import FastAPI


app = FastAPI()



@app.get('/')
def index():
    return { "data": 'shit' }



@app.get('/about')
def about():
    return {'data': 'about page'}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)