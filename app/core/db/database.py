from collections.abc import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker

from ..config import settings


class Base(DeclarativeBase, MappedAsDataclass):
    pass


DATABASE_URI = settings.DATABASE_URI
DATABASE_PREFIX = settings.DATABASE_ASYNC_PREFIX
DATABASE_URL = f"{DATABASE_PREFIX}{DATABASE_URI}"

async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

local_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def async_get_db() -> AsyncGenerator[AsyncSession, None]:
    async_session = local_session
    async with async_session() as db:
        yield db


async def test_connection():
    async for db in async_get_db():
        try:
            result = await db.execute(text("SELECT 1"))
            print("Connection successful:", result.scalar() == 1)
        except Exception as e:
            print("Connection failed:", e)
