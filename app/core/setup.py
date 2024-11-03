from quart import Quart
from quart_schema import QuartSchema

from app.api.routes import router

app = Quart(__name__)
QuartSchema(app, info={"title": "Quart API", "version": "0.1.0"})
app.register_blueprint(router)

def create_app():
    return app
