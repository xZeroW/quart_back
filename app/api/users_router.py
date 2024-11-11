from quart import Blueprint, g
from quart_schema import tag, validate_response
from sqlalchemy.future import select

from app.models import User
from app.schemas import UserResponseSchema

users_blueprint = Blueprint("users", __name__, url_prefix="/user")


@users_blueprint.get("")
@validate_response(list[UserResponseSchema])
@tag(["Users"])
async def get_user() -> list[UserResponseSchema]:
    result = await g.db.execute(select(User))
    users = result.scalars().all()
    users_response = [UserResponseSchema.model_validate(user) for user in users]
    return users_response
