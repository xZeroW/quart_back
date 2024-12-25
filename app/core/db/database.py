from quart import abort, request
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.customer_connections_model import CustomersConnections

painel_engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
painel_session = sessionmaker(bind=painel_engine, class_=AsyncSession, expire_on_commit=False)


async def get_user_db_session() -> AsyncSession:
    data = await request.get_json()

    if not data or "account_id" not in data:
        abort(400, description="The 'account_id' field is required in the request body.")

    account_id = data["account_id"]

    try:
        async with painel_session() as session:
            result = await session.execute(
                select(CustomersConnections).where(CustomersConnections.account_id == account_id)
            )
            db = result.scalar()

            if not db:
                abort(404, description="No user found with the specified account_id.")

            user_database_url = (
                f"{settings.DATABASE_ASYNC_PREFIX}{db.database_username}:{db.database_password}@"
                f"{db.database_host}:{db.database_port}/{db.database_name}"
            )

            user_async_engine = create_async_engine(user_database_url, echo=False, future=True)

            return sessionmaker(bind=user_async_engine, class_=AsyncSession, expire_on_commit=False)()

    except Exception:
        abort(503)