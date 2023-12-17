from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from auth import schemas
from auth.models import product  # Замените на свое название модели
from auth.schemas import ProductCreate, ProductUpdate

async def create_product(db: AsyncSession, product_create: ProductCreate):
    db_product = product_create.dict()
    await db.execute(product.insert().values(**db_product))
    await db.commit()
    return product_create

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await db.execute(product.select().offset(skip).limit(limit)).fetchall()

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
async def delete_product(db: AsyncSession, product_id: int):
    db_product = await db.execute(product.select().where(product.c.id == product_id)).fetchone()
    await db.execute(product.delete().where(product.c.id == product_id))
    await db.commit()
    return db_product