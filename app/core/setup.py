from quart import Blueprint, Quart
from quart_schema import QuartSchema

from app.core.config import (
    AppSettings,
    AWSSettings,
    ClientSideCacheSettings,
    CryptSettings,
    DatabaseSettings,
    DiskSettings,
    EnvironmentOption,
    EnvironmentSettings,
    SMTPSettings,
    TestSettings,
)
from app.core.error_handlers import register_error_handlers
from app.core.middleware import db_session_middleware


def create_app(
    router: Blueprint,
    settings: (
        DatabaseSettings
        | CryptSettings
        | AppSettings
        | DiskSettings
        | ClientSideCacheSettings
        | AWSSettings
        | SMTPSettings
        | TestSettings
        | EnvironmentOption
        | EnvironmentSettings
    ),
) -> Quart:
    """Create and configure the Quart application.

    Args:
        router (Blueprint): The main router blueprint to register.
        settings: Configuration settings object, supporting various environment configurations.

    Returns:
        Quart: Configured Quart application instance.
    """
    app = Quart(__name__)

    db_session_middleware(app)
    QuartSchema(app, info={"title": "Quart API", "version": "0.1.0"})  # TODO: descobrir como desativar docs em produção

    app.register_blueprint(router)

    is_production = settings.ENVIRONMENT == EnvironmentOption.PRODUCTION
    register_error_handlers(app, is_production)

    return app
