import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import AsyncClient

from src.app import app
from .fixtures import bags_mock, orders_mock


def test_ping():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
@pytest.mark.server(url="/orders/", response=orders_mock, method="GET")
@pytest.mark.server(url="/bags/", response=bags_mock, method="PUT")
async def test_ski_transport_request_ok():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {"number": "AAAAAA", "passengerId": "ivanov"}
        response = await ac.post("/api/ski_transport_request", json=body)

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("shoppingCart") == bags_mock.get("shoppingCart")


@pytest.mark.asyncio
async def test_ski_transport_request_validation_fail():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        body = {"number": "AAAAAA"}
        response = await ac.post("/api/ski_transport_request", json=body)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "passengerId"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
