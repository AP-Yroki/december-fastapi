from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    subcategory = Column(String)
    manufacturer = Column(String)
    characteristics = Column(String)  # JSON field or separate columns
    price = Column(Float)
    availability = Column(Integer)
    photos = relationship("ProductPhoto", back_populates="product")

class ProductPhoto(Base):
    __tablename__ = 'product_photos'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="photos")
