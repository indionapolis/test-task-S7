from fastapi import APIRouter

from src.booking_service import BookingService
from src.datamodels import OrdersRequest, Bags
from src.dataparser import DataParser

router = APIRouter()
booking_service = BookingService("http://localhost:5000/")
data_parser = DataParser()


@router.post("/ski_transport_request", response_model=Bags)
async def ski_transport_request(request: OrdersRequest):
    orders = await booking_service.get_orders(request)
    bags_request = data_parser.pars_sky_orders(orders)
    response = await booking_service.add_bags(bags_request)
    return response
