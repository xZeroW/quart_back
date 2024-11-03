from pydantic import BaseModel, Field

class HelloWorldModel(BaseModel):
    msg: str = Field(..., example='Hello World')