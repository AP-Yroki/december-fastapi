from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix='/account',
    tags=['account']
)

templates = Jinja2Templates(directory='templates')



@router.get("/registration", response_class=HTMLResponse)
def get_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
def get_signup(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


