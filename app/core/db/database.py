from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

DATABASE_URI = settings.DATABASE_URI
DATABASE_PREFIX = settings.DATABASE_ASYNC_PREFIX
DATABASE_URL = f"{DATABASE_PREFIX}{DATABASE_URI}"

async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

local_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def async_get_db() -> AsyncGenerator[AsyncSession, None]:
    async_session = local_session()
    async with async_session as db:
        yield db
