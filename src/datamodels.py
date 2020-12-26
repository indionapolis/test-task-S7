from typing import List

from pydantic import BaseModel


class OrdersRequest(BaseModel):
    number: str
    passengerId: str


class BaggageSelection(BaseModel):
    passengerId: str
    routeId: str
    baggageIds: List[str]
    redemption: bool = False


class BagsRequest(BaseModel):
    baggageSelections: List[BaggageSelection] = None


class Bags(BaseModel):
    shoppingCart: dict = None
    error: dict = None


class Baggage(BaseModel):
    id: str
    overWeight: bool
    amount: int
    unit: str
    weight: dict = dict()
    code: str
    descriptions: List
    registered: bool
    equipmentType: str = None


class BaggagePricings(BaseModel):
    passengerIds: List[str]
    passengerTypes: List[str]
    purchaseType: str
    routeId: str
    baggages: List[Baggage]


class AncillariesPricings(BaseModel):
    airId: str
    baggagePricings: List[BaggagePricings]


class Orders(BaseModel):
    ancillariesPricings: List[AncillariesPricings]
