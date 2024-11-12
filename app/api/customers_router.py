from quart import Blueprint, g
from quart_schema import tag, validate_response
from sqlalchemy.future import select

from app.models import Customer
from app.schemas import CustomerResponseSchema

customers_blueprint = Blueprint("customers", __name__, url_prefix="/customer")


@customers_blueprint.get("")
@validate_response(list[CustomerResponseSchema])
@tag(["Customers"])
async def get_user() -> list[CustomerResponseSchema]:
    result = await g.db.execute(select(Customer))
    customers = result.scalars().all()
    customers_response = [CustomerResponseSchema.model_validate(user) for user in customers]
    return customers_response
