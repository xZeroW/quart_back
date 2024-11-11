import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped, mapped_column


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True, unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
