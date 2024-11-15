from typing import Optional

from app.schemas.base_schema import BaseSchema


class LoginRequestSchema(BaseSchema):
    account_id: str
    email: str
    password: str
    current_sign_in_ip: str
    user_first_key: Optional[str]
