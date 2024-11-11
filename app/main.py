import asyncio

from app.api import router
from app.core.config import settings
from app.core.setup import create_app

app = create_app(router, settings)

if __name__ == "__main__":
    asyncio.run(app.run_task(host="0.0.0.0", port=5000))
