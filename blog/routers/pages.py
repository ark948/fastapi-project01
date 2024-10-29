from fastapi import APIRouter, status, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)


templates = Jinja2Templates(directory="templates")


@router.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html', context={'message': "WORLD"}
    )