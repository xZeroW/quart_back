from pydantic import BaseModel, Field


class HelloWorldResponseSchema(BaseModel):
    msg: str = Field(default='Hello World')
