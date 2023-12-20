from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base



metadata = MetaData()
Base = declarative_base()



role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)




item = Table(
    'item',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("item_type", String, nullable=False),
    Column("item_subtype", String, nullable=False),
    Column("manufacturer", String, nullable=False),
    Column("characteristics", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("availability", Integer, nullable=False),
    Column("photo_url", String, nullable=False),

)


product = Table(
    'product',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_name", String, index=True),
    Column("tech_type", String),
    Column("tech_variation", String),
    Column("manufacturer", String),
    Column("product_characteristics", String),
    Column("price", Float),
    Column("availability", Integer),
    Column("photo_url", String),

)


order = Table(
    'order',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey('user.id'), nullable=False),
    Column("order_name", String),
    Column("status", String),
    Column("delivery_type", String),
    Column("delivery_location", String),
    Column("payment_method", String),
    Column("delivery_date", TIMESTAMP),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
)