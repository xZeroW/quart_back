import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Base(SQLModel):
    id: uuid.UUID = Field(default=uuid.uuid4(), primary_key=True, index=True)
    created_at: datetime = Field(default=None)
    updated_at: Optional[datetime] = Field(default=None)
    deleted_at: Optional[datetime] = Field(default=None)
