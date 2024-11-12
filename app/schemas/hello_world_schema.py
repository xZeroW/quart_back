from pydantic import Field

from app.schemas.base_schema import BaseSchema


class HelloWorldResponseSchema(BaseSchema):
    msg: str = Field(default="Hello World")
