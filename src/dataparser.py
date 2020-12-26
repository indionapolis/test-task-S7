from src.datamodels import BagsRequest, Orders


class DataParser:
    @staticmethod
    def pars_sky_orders(orders: Orders) -> BagsRequest:
        """
        method to transform Orders into BagsRequest
        @param orders: number of orders
        @return: baggageSelections
        """
        baggageSelections = []
        for ancillariesPricing in orders.ancillariesPricings:
            for baggagePricing in ancillariesPricing.baggagePricings:
                for passenger in baggagePricing.passengerIds:
                    for baggage in baggagePricing.baggages:
                        tmp = {
                            "passengerId": passenger,
                            "routeId": baggagePricing.routeId,
                            "baggageIds": [],
                        }
                        if baggage.equipmentType == "ski":
                            tmp["baggageIds"].append(baggage.id)

                    if tmp["baggageIds"]:
                        baggageSelections.append(tmp)

        baggageSelections.sort(key=lambda x: x.get("passengerId"))
        return BagsRequest(baggageSelections=baggageSelections)
