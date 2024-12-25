from quart import Blueprint
from quart_schema import tag, validate_request

from app.core.middleware import session_middleware
from app.schemas import LoginRequestSchema

login_blueprint = Blueprint("login", __name__)


@login_blueprint.post("/login")
@validate_request(LoginRequestSchema)
@tag(["Login"])
@session_middleware
async def login(data: LoginRequestSchema) -> str:
    return "OK"


@login_blueprint.post("/sysadmin")
@tag(["Login"])
@session_middleware
async def sysadmin_login(): ...
