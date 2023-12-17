from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    subcategory: str
    manufacturer: str
    characteristics: str
    price: float
    availability: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
