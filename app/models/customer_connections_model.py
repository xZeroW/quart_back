import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


class CustomersConnections(Base):
    __tablename__ = "customers_connections"

    customer_id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, unique=True, index=True)
    account_id: Mapped[str] = mapped_column()
    database_host: Mapped[str] = mapped_column()
    database_port: Mapped[int] = mapped_column()
    database_name: Mapped[str] = mapped_column()
    database_username: Mapped[str] = mapped_column()
    database_password: Mapped[str] = mapped_column()
