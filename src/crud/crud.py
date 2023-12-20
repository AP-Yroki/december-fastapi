from http.client import HTTPException

from fastapi import Depends
from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.sql import select
from auth import schemas
from auth.models import product
from auth.schemas import ProductCreate, ProductUpdate




from pydantic import BaseModel

from database import get_db


class SuccessResponse(BaseModel):
    message: str


async def create_product(db: AsyncSession, product_create: ProductCreate):
    db_product = product_create.dict()
    await db.execute(product.insert().values(**db_product))
    await db.commit()
    return product_create

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    products = await db.execute(product.select().offset(skip).limit(limit))
    return products.fetchall()


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(product.select().where(product.c.id == product_id))
    return result.fetchone()


async def update_product(db: AsyncSession, product_id: int,
                         product_update: schemas.ProductUpdate):
    await db.execute(
        product.update().where(product.c.id == product_id).values(
            product_update.dict(exclude_unset=True))
    )
    await db.commit()

    # Retrieve the updated product using an asynchronous query
    updated_product = await get_product(db, product_id)

    return updated_product
async def delete_product(db: AsyncSession, product_id: int, product=product):
    try:
        # Найти продукт по идентификатору
        product_to_delete = await db.execute(product.select().where(product.c.id == product_id))
        # Удалить продукт
        await db.execute(delete(product).where(product.c.id == product_id))
        # Подтвердить изменения в базе данных
        await db.commit()
        return {'message': 'Товар успешно удален'}
    except SQLAlchemyError as e:
        # Обработка ошибок, например, логирование
        print(f"Error deleting product: {e}")
        await db.rollback()
        return {'message': 'Произошла ошибка при удалении товара'}

