from asyncio import sleep

import uvicorn
from fastapi import FastAPI

from src.datamodels import BagsRequest

mock_app = FastAPI()

orders_mock = {
    "ancillariesPricings": [
        {
            "airId": "ef8ff876-9b29-448f-97ba-094898deef98",
            "baggagePricings": [
                {
                    "passengerIds": ["dKCLeweYNb6iDO66", "qauJTpuMlDrASaty"],
                    "passengerTypes": ["ADT"],
                    "purchaseType": "PAID",
                    "routeId": "RyucZ4TVI1EseYCp",
                    "baggages": [
                        {
                            "id": "nqNNipOwlK7i9fRr",
                            "overWeight": True,
                            "amount": 1,
                            "unit": "KG",
                            "weight": {"amount": 50, "unit": "KG"},
                            "code": "0IK",
                            "descriptions": ["EXCESS WEIGHT"],
                            "registered": False,
                        },
                        {
                            "id": "q0YIbjcv2zSx4JGK",
                            "overWeight": False,
                            "amount": 1,
                            "unit": "PC",
                            "weight": {"amount": 23, "unit": "KG"},
                            "code": "0CC",
                            "descriptions": ["CHECKED BAG FIRST"],
                            "registered": False,
                        },
                        {
                            "id": "KChsLeEHhHqEvGmw",
                            "overWeight": False,
                            "amount": 2,
                            "unit": "PC",
                            "weight": {"amount": 23, "unit": "KG"},
                            "code": "0CD",
                            "descriptions": ["CHECKED BAG SECOND"],
                            "registered": False,
                        },
                        {
                            "id": "siEct88JoxGWpe5v",
                            "overWeight": False,
                            "amount": 1,
                            "unit": "PC",
                            "code": "0DD",
                            "descriptions": ["SNOW SKI SNOWBOARD EQUIPMENT"],
                            "registered": False,
                            "equipmentType": "ski",
                        },
                    ],
                },
                {
                    "passengerIds": ["dKCLeweYNb6iDO66", "qauJTpuMlDrASaty"],
                    "passengerTypes": ["ADT"],
                    "purchaseType": "PAID",
                    "routeId": "iqCrFYw8oDTwVpWD",
                    "baggages": [
                        {
                            "id": "xawp8dUZHYaJqmVS",
                            "overWeight": True,
                            "amount": 1,
                            "unit": "KG",
                            "weight": {"amount": 50, "unit": "KG"},
                            "code": "0IK",
                            "descriptions": ["EXCESS WEIGHT"],
                            "registered": False,
                        },
                        {
                            "id": "AzD5GiHPkxVruI3B",
                            "overWeight": False,
                            "amount": 1,
                            "unit": "PC",
                            "weight": {"amount": 23, "unit": "KG"},
                            "code": "0CC",
                            "descriptions": ["CHECKED BAG FIRST"],
                            "registered": False,
                        },
                        {
                            "id": "7UPUB3KhGSI12ZXF",
                            "overWeight": False,
                            "amount": 2,
                            "unit": "PC",
                            "weight": {"amount": 23, "unit": "KG"},
                            "code": "0CD",
                            "descriptions": ["CHECKED BAG SECOND"],
                            "registered": False,
                        },
                        {
                            "id": "CMQs0BgMVGpAJcOP",
                            "overWeight": False,
                            "amount": 1,
                            "unit": "PC",
                            "code": "0DD",
                            "descriptions": ["SNOW SKI SNOWBOARD EQUIPMENT"],
                            "registered": False,
                            "equipmentType": "ski",
                        },
                    ],
                },
            ],
            "baggageDisabled": False,
            "seatsDisabled": False,
            "mealsDisabled": False,
            "upgradesDisabled": True,
            "loungesDisabled": False,
            "fastTracksDisabled": False,
            "petsDisabled": True,
        }
    ]
}


@mock_app.get("/orders")
def orders(number: str, passengerId: str):
    return orders_mock


@mock_app.put("/bags")
async def orders(request: BagsRequest):
    # simulate long calculation
    await sleep(6)
    return {
        "shoppingCart": request,
    }


def run_mock_app():
    uvicorn.run(mock_app, port=5000)
