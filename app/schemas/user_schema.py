from uuid import UUID

from pydantic import EmailStr

from app.schemas.base_schema import BaseSchema


class UserResponseSchema(BaseSchema):
    id: UUID
    name: str
    _email: EmailStr
    profile_image: str
