from quart import Blueprint, Quart
from quart_schema import QuartSchema

from .config import (
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


def create_app(router: Blueprint, settings: (
        DatabaseSettings
        | CryptSettings
        | AppSettings
        | DiskSettings
        | ClientSideCacheSettings
        | AWSSettings
        | SMTPSettings
        | TestSettings
        | EnvironmentSettings
    )):

    app = Quart(__name__)

    if isinstance(settings, EnvironmentSettings):
        if settings.ENVIRONMENT != EnvironmentOption.PRODUCTION:
            QuartSchema(app, info={"title": "Quart API", "version": "0.1.0"})

    app.register_blueprint(router)

    return app
