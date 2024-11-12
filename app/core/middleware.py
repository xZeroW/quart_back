from quart import Quart, g

from app.core.db.database import get_user_db_session


def db_session_middleware(app: Quart):
    @app.before_request
    async def start_session():
        g.db = await get_user_db_session()

    @app.after_request
    async def cleanup_session(response):
        db = g.pop("db", None)
        if db is not None:
            await db.close()
        return response
