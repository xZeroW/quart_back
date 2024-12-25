from quart import g
from functools import wraps

from app.core.db.database import get_user_db_session

def session_middleware(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Middleware logic before the route handler
        try:
            print("Starting session")
            g.db = await get_user_db_session()
            # Call the original route handler
            response = await func(*args, **kwargs)
        finally:
            # Middleware logic after the route handler
            print("Cleaning session")
            db = g.pop("db", None)
            if db is not None:
                await db.close()
        return response
    return wrapper