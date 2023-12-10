from fastapi import APIRouter, Request, Depends, FastAPI
from fastapi.templating import Jinja2Templates

from fastapi_users import FastAPIUsers
from fastapi.responses import HTMLResponse
from database import User
from auth.manager import get_user_manager
from auth.base_config import auth_backend



fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

router = APIRouter(
    prefix='',
    tags=['home']
)

templates = Jinja2Templates(directory='templates')




@router.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/home", response_class=HTMLResponse)
async def read_main(request: Request, user: User = Depends(current_user)):
    return templates.TemplateResponse("home.html", {"request": request, 'user': user})
