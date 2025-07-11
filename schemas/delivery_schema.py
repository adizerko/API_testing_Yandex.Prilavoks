from pydantic import BaseModel, RootModel


class ToBeDeliveredTime(BaseModel):
    min: int
    max: int


class DeliveryResponse(BaseModel):
    name: str
    isItPossibleToDeliver: bool
    hostDeliveryCost: int
    toBeDeliveredTime: ToBeDeliveredTime
    clientDeliveryCost: int
