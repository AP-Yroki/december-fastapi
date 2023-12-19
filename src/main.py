from typing import List

from fastapi_users import FastAPIUsers
from fastapi import Depends, FastAPI, HTTPException, Request, File, UploadFile, \
    Form, status
from pydantic import BaseModel

from auth.base_config import auth_backend
from database import User, sessionlocal
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from registration.router import router as router_signup
from homepage.router import router as router_homepage
from crud.router import router as crud_router
from fastapi.templating import Jinja2Templates

# from database import SessionLocal



app = FastAPI(
    title='Online Shop'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_signup)
app.include_router(router_homepage)
app.include_router(crud_router)

current_user = fastapi_users.current_user()

# Templates for HTML rendering
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8",
                              decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.post("/api/cart/add/{product_id}")
def add_to_cart(product_id: int):
    # Здесь должна быть логика добавления товара в корзину пользователя
    # Например, сохранение информации в базу данных или в сессию пользователя
    # Верните подтверждение успешного добавления товара
    return {"message": "Товар успешно добавлен в корзину"}


class CartItem(BaseModel):
    product_id: int
    quantity: int


cart_items = {}

@app.post("/api/cart/add/{product_id}")
def add_to_cart(product_id: int, item: CartItem):
    # Здесь должна быть логика добавления товара в корзину
    # Например, обновление словаря cart_items
    if product_id in cart_items:
        cart_items[product_id]['quantity'] += item.quantity
    else:
        cart_items[product_id] = {'product_id': product_id, 'quantity': item.quantity}

    # Верните подтверждение успешного добавления товара
    return {"message": "Товар успешно добавлен в корзину"}

@app.get("/api/cart")
def view_cart():
    # Здесь должна быть логика получения данных о корзине пользователя
    # Например, извлечение данных из словаря cart_items
    return cart_items



def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

