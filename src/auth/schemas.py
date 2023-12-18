from fastapi_users import schemas
from pydantic import BaseModel
from typing import Optional



class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False




class ProductBase(BaseModel):
    product_name: str
    tech_type: str
    tech_variation: str
    manufacturer: str
    product_characteristics: str
    price: float
    availability: int
    photo_url: Optional[str]

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True