import pytest
from app.api.hello_router import hello_blueprint
from app.main import app

@pytest.mark.asyncio
async def test_hello_world():
    async with app.test_client() as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert await response.get_json() == {"msg": "Hello World"}
