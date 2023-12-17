from typing import List

from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi_users import FastAPIUsers
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session

from database import get_async_session
from . import crud, schemas
from database import get_db
from auth.manager import get_user_manager
from auth.base_config import auth_backend
from auth.models import user as User  # Добавлен импорт User

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

router = APIRouter(
    prefix='',
    tags=['home']
)

templates = Jinja2Templates(directory='templates')

@router.get("/test", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("testindex.html", {"request": request})

# @router.get("/testhome", response_class=HTMLResponse)
# async def read_main(request: Request, user: User = Depends(current_user)):  # Используем User из auth.models
#     return templates.TemplateResponse("testhome.html", {"request": request, 'user': user})
#
# @router.post("/products/", response_model=schemas.Product)
# async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_async_session)):
#     try:
#         return await crud.create_product(db=db, product=product)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
