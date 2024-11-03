from quart import Blueprint
from quart_schema import tag

users_blueprint = Blueprint('users', __name__, url_prefix='/user')

@users_blueprint.get('')
@tag(['Users'])
async def get_user() -> str:
    return 'this is a user'
