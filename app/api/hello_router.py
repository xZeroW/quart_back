from quart import Blueprint
from quart_schema import tag, validate_response

from app.schemas import HelloWorldResponseSchema

hello_blueprint = Blueprint("hello", __name__, url_prefix="/")


@hello_blueprint.get("")
@validate_response(HelloWorldResponseSchema)
@tag(["/"])
async def hello_world() -> HelloWorldResponseSchema:
    return {"msg": "Hello World"}, 200
