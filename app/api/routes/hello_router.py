from quart import Blueprint
from quart_schema import tag, validate_response

from app.models.hello_world import HelloWorldModel

hello_blueprint = Blueprint('hello', __name__, url_prefix='/')

@hello_blueprint.get('')
@validate_response(HelloWorldModel)
@tag(['/'])
async def hello_world() -> HelloWorldModel:
    return {'msg': 'Hello World'}, 200
