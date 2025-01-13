from quart import Blueprint, Quart
from quart_cors import cors
from quart_schema import QuartSchema
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

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
    app = cors(app)

    app.register_blueprint(router)

    is_production = settings.ENVIRONMENT == EnvironmentOption.PRODUCTION
    doc_path = None if is_production else "/openapi.json"
    QuartSchema(app, openapi_path=doc_path, info={"title": "Quart API", "version": "0.1.0"})
    register_error_handlers(app, is_production)

    @app.before_serving
    async def startup():
        try:
            print("Creating database tables...")
            engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
            async with engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.create_all)
        except Exception as e:
            print(f"Error creating database tables: {e}")

    return app
