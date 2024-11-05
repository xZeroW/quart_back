import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column()
    profile_image: Mapped[str] = mapped_column()
    encrypted_password: Mapped[str] = mapped_column()
    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"), index=True)
    failed_attempts: Mapped[int] = mapped_column(default=0)
    notification: Mapped[bool] = mapped_column(default=True)
    role: Mapped[str | None] = mapped_column(default=None)
    sign_in_count: Mapped[int] = mapped_column(default=0)
    change_password: Mapped[bool] = mapped_column(default=False)
    reset_password_token: Mapped[str | None] = mapped_column(default=None)
    reset_password_sent_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    remember_created_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    unlock_token: Mapped[str | None] = mapped_column(default=None)
    locked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    current_sign_in_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    last_sign_in_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    current_sign_in_ip: Mapped[str | None] = mapped_column(default=None)
    last_sign_in_ip: Mapped[str | None] = mapped_column(default=None)
    status: Mapped[str] = mapped_column(default="active")
    user_profile_id: Mapped[uuid.UUID | None] = mapped_column()
    unique_session_id: Mapped[str | None] = mapped_column(default=None)
    actived_session: Mapped[bool] = mapped_column(default=False)
    task_manager_profile_id: Mapped[uuid.UUID | None] = mapped_column()
    allow_manager_task: Mapped[bool] = mapped_column(default=False)
    super_user: Mapped[bool] = mapped_column(default=False)
    phone: Mapped[str | None] = mapped_column(default=None)
    enable_two_factor_auth: Mapped[bool] = mapped_column(default=False)
    first_user_key: Mapped[str | None] = mapped_column(default=None)
