import asyncio

from .core.setup import create_app

app = create_app()

if __name__ == '__main__':
    asyncio.run(app.run_task(host='0.0.0.0', port=5000))
