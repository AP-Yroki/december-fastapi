from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session, get_db
from auth.models import product  # Замените на свое название модели
from auth.schemas import ProductCreate, ProductUpdate
from .crud import create_product, get_products, get_product, update_product, \
    delete_product, SuccessResponse

router = APIRouter()

@router.post("/products/", response_model=ProductCreate)
async def create_product_route(product_create: ProductCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_product(db=db, product_create=product_create)

@router.get("/products/", response_model=list[ProductCreate])
async def get_products_route(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session)):
    return await get_products(db=db, skip=skip, limit=limit)

@router.get("/products/{product_id}", response_model=ProductCreate)
async def get_product_route(product_id: int, db: AsyncSession = Depends(get_async_session)):
    product_data = await get_product(db=db, product_id=product_id)
    if product_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product_data

@router.put("/products/update/{product_id}", response_model=ProductCreate)
async def update_product_route(product_id: int, product_update: ProductUpdate, db: AsyncSession = Depends(get_async_session)):
    return await update_product(db=db, product_id=product_id, product_update=product_update)

@router.delete("/products/delete/{product_id}", response_model=SuccessResponse)
async def delete_product_route(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await delete_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return db_product

