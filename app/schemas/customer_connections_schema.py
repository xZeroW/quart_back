from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.schemas.base_schema import BaseSchema


class CustomersConnectionsSchema(BaseSchema):
    id: UUID
    customer_id: UUID
    account_id: str
    database_host: str
    database_port: int
    database_name: str
    database_username: str
    database_password: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class CustomersConnectionsResponseSchema(CustomersConnectionsSchema):
    pass


class CustomersConnectionsCreateSchema(BaseSchema):
    account_id: str
    database_host: str
    database_port: int
    database_name: str
    database_username: str
    database_password: str
    created_at: datetime = Field(default_factory=datetime.now)
