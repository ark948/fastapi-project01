from fastapi import APIRouter, status, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)