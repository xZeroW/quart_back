from quart import Blueprint
from quart_schema import tag, validate_response
from sqlalchemy.future import select

from app.core.db.database import async_get_db
from app.models import User
from app.schemas import UserResponseSchema

users_blueprint = Blueprint("users", __name__, url_prefix="/user")


@users_blueprint.get("")
@validate_response(list[UserResponseSchema])
@tag(["Users"])
async def get_user() -> list[UserResponseSchema]:
    async with async_get_db() as db:
        result = await db.execute(select(User))
        users = result.scalars().all()
        users_response = [UserResponseSchema.model_validate(user) for user in users]
        return users_response
