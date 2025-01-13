from quart import Blueprint

from app.api.customer_connections_router import customer_connections_blueprint
from app.api.customers_router import customers_blueprint
from app.api.hello_router import hello_blueprint
from app.api.login_router import login_blueprint
from app.api.users_router import users_blueprint

router = Blueprint("router", __name__)
router.register_blueprint(users_blueprint)
router.register_blueprint(hello_blueprint)
router.register_blueprint(customers_blueprint)
router.register_blueprint(login_blueprint)
router.register_blueprint(customer_connections_blueprint)
