import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlmodel import Field

from app.models.base_model import Base
from app.models.customer_model import Customer


class User(Base, table=True):
    __tablename__ = "users"

    email: str = Field(String(50), unique=True)
    name: str
    profile_image: str
    encrypted_password: str
    customer_id: uuid.UUID = Field(ForeignKey(Customer.id), index=True)
    failed_attempts: int = Field(default=0)
    notification: bool = Field(default=True)
    role: Optional[str] = Field(default=None)
    sign_in_count: int = Field(default=0)
    change_password: bool = Field(default=False)
    reset_password_token: Optional[str] = Field(default=None)
    reset_password_sent_at: Optional[datetime] = Field(default=None)
    remember_created_at: Optional[datetime] = Field(default=None)
    unlock_token: Optional[str] = Field(default=None)
    locked_at: Optional[datetime] = Field(default=None)
    current_sign_in_at: Optional[datetime] = Field(default=None)
    last_sign_in_at: Optional[datetime] = Field(default=None)
    current_sign_in_ip: Optional[str] = Field(default=None)
    last_sign_in_ip: Optional[str] = Field(default=None)
    status: str = Field(default="active")
    user_profile_id: Optional[uuid.UUID]
    unique_session_id: Optional[str] = Field(default=None)
    actived_session: bool = Field(default=False)
    task_manager_profile_id: Optional[uuid.UUID]
    allow_manager_task: bool = Field(default=False)
    super_user: bool = Field(default=False)
    phone: Optional[str] = Field(default=None)
    enable_two_factor_auth: bool = Field(default=False)
    first_user_key: Optional[str] = Field(default=None)
