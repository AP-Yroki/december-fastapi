from datetime import datetime
from typing import AsyncGenerator, Generator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, ForeignKey, Float

from sqlalchemy.orm import Session

# Correct import assuming `role` is in the same module
from auth.models import role
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/postgres2"

engine = create_async_engine(DATABASE_URL, echo=True)
metadata = MetaData()
Base = declarative_base()

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_db():
    db = AsyncSession(engine)
    try:
        yield db
    finally:
        await db.close()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)