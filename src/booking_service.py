from multiprocessing import Process
from urllib.parse import urljoin

import aiohttp
import pydantic

from src.datamodels import BagsRequest, OrdersRequest, Orders, Bags
from src.mocks import run_mock_app

# needed for requesting mocked data
proc = Process(target=run_mock_app, args=(), daemon=True)
proc.start()


class BookingServiceError(Exception):
    """
    This error generated whenever outgoing or ingoing data dose not
    correspond to expected schemas or when external service is out of service
    """


class BookingServiceValidationError(BookingServiceError):
    def __init__(self, error):
        self.error = error
        super().__init__(str(error))

    @staticmethod
    def error_wrapper(function):
        async def wrapper(*args, **kwargs):
            try:
                result = await function(*args, **kwargs)
            except pydantic.error_wrappers.ValidationError as e:
                raise BookingServiceValidationError(e)
            else:
                return result

        return wrapper


class BookingService:
    def __init__(self, base_url):
        self.url = base_url

    @BookingServiceValidationError.error_wrapper
    async def get_orders(self, request: OrdersRequest) -> Orders:
        """
        method to retrieve order information for particular person on particular order
        @param request: request information
        @return: response from service or exception
        """
        result = await self._make_request("GET", "/orders", params=request.dict())
        return Orders(**result)

    @BookingServiceValidationError.error_wrapper
    async def add_bags(self, request: BagsRequest) -> Bags:
        """
        method to add bags to the booking
        @param request: request information
        @return: response from service or exception
        """
        result = await self._make_request("PUT", "/bags", json=request.dict())
        return Bags(**result)

    async def _make_request(self, method, endpoint, **kwargs) -> dict:
        request_url = urljoin(self.url, endpoint)

        async with aiohttp.ClientSession() as session:
            async with session.request(method, request_url, **kwargs) as response:
                if response.ok:
                    return await response.json()
                else:
                    raise BookingServiceError(response.text)
