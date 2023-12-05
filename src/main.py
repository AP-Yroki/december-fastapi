from typing import Union
from fastapi_users import FastAPIUsers
from fastapi import Depends, FastAPI, HTTPException, Request, File, UploadFile, \
    Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse

from auth.base_config import auth_backend
from database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from registration.router import router as router_signup
from homepage.router import router as router_homepage



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


current_user = fastapi_users.current_user()

# Templates for HTML rendering
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8",
                              decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")



@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"