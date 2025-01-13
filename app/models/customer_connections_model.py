import uuid

from sqlmodel import Field

from app.models.base_model import Base


class CustomersConnectionsBase(Base):
    customer_id: uuid.UUID = Field(default=uuid.uuid4(), unique=True, index=True)
    account_id: str
    database_host: str
    database_port: int
    database_name: str
    database_username: str
    database_password: str


class CustomersConnections(CustomersConnectionsBase, table=True):
    __tablename__ = "customers_connections"


class CustomersConnectionsCreate(CustomersConnectionsBase):
    pass
