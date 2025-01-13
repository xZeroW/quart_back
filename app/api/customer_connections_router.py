from quart import Blueprint
from quart_schema import tag, validate_request, validate_response
from sqlalchemy.future import select

from app.core.database import painel_session
from app.models.customer_connections_model import CustomersConnections, CustomersConnectionsCreate

customer_connections_blueprint = Blueprint("customer connections", __name__, url_prefix="/customerconnections")


@customer_connections_blueprint.get("")
@validate_response(list[CustomersConnections])
@tag(["CustomerConnections"])
async def get_customer_connections() -> list[CustomersConnections]:
    async with painel_session() as session:
        result = await session.execute(select(CustomersConnections))
        customers = result.scalars().all()
        customers_response = [CustomersConnections.model_validate(user) for user in customers]
        return customers_response


@customer_connections_blueprint.post("")
@validate_request(CustomersConnectionsCreate)
@validate_response(CustomersConnections)
@tag(["CustomerConnections"])
async def create_customer_connection(data: CustomersConnectionsCreate) -> CustomersConnectionsCreate:
    async with painel_session() as session:
        session.add(CustomersConnections(**data.dict()))
        await session.commit()
        return CustomersConnectionsCreate.model_validate(data)
