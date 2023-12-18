from http.client import HTTPException

from fastapi import APIRouter, Request, Depends, FastAPI
from fastapi.templating import Jinja2Templates

from fastapi_users import FastAPIUsers
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from crud.crud import get_products
from database import User, sessionlocal, async_session, async_session_maker, \
    get_db
from auth.manager import get_user_manager
from auth.base_config import auth_backend
from auth.models import product


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

#
# @router.get("/home", response_class=HTMLResponse)
# async def read_main(request: Request, user: User = Depends(current_user)):
#     products = get_all_products()
#     return templates.TemplateResponse("home.html", {"request": request, 'user': user, "items": products})



@router.get("/home", response_class=HTMLResponse)
async def read_root(request: Request, user: User = Depends(current_user)):
    async with async_session_maker() as session:
        products = await get_products(session)
        return templates.TemplateResponse("home.html", {"request": request, "products": products, 'user': user,})



async def get_all_products():
    async with async_session() as db:
        products = await db.execute(product.select()).scalars().all()
    return products


