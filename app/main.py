import asyncio

from .api import router
from .core.config import settings
from .core.setup import create_app

app = create_app(router=router, settings=settings)

if __name__ == "__main__":
    asyncio.run(app.run_task(host="0.0.0.0", port=5000))
