from quart import Blueprint

from .hello_router import hello_blueprint
from .users_router import users_blueprint

router = Blueprint('router', __name__)
router.register_blueprint(users_blueprint)
router.register_blueprint(hello_blueprint)
