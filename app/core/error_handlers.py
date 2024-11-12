from quart import Quart
from quart_schema import RequestSchemaValidationError, ResponseSchemaValidationError


def register_error_handlers(app: Quart, production: bool = False):
    def format_validation_error(e, status_code: int):
        if production:
            return {"error": "VALIDATION"}, status_code
        else:
            return str(e.validation_error), status_code

    @app.errorhandler(ResponseSchemaValidationError)
    async def handle_response_validation_error(e):
        return format_validation_error(e, 500)

    @app.errorhandler(RequestSchemaValidationError)
    async def handle_request_validation_error(error):
        return format_validation_error(error, 400)
