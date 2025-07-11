import pytest
import config.settings
from utils.api_client import APIClient
from schemas.delivery_schema import DeliveryResponse


client = APIClient()


BROOMSTICK_DELIVERY = "На метле уюта"
DELIVERY_TIME = "deliveryTime"
PRODUCTS_COUNT = "productsCount"
PRODUCTS_WEIGHT = "productsWeight"


PAYLOAD_DATA = {
    "productsCount": {
        "positive": {
            "0-9": [0, 1, 4, 8, 9],
            "10-15": [10,11, 13, 14, 15],
            "16-30": [16, 17, 20, 29, 30]},
        "negative": [-1, -5, "" , 1234245343423, "sd", "#@", "4-3", "4 4", -15, 12.0]},
    
    "productsWeight": {
        "positive": {
            "0-3": [0, 0.1, 1.5, 2.9, 3.0, 3],
            "3.1-6": [3.1, 3.2, 4.2, 5.8, 5.9, 6, 6.0],
            "6.1-10": [6.1, 6.2, 7.6, 9.9, 10, 10.0]},        
        "negative": ["sd", "#@", "4-3", "4 4", -15, 1234124123214241, -0.1, ""]},
    
    "deliveryTime": {
        "positive": [8, 9, 15, 21, 22],
        "negative": [6, 7, 23, 24, 25, 44, 343442133123214444, -5, 15.5, "sd", "#@", "4-3", "4 4", ""]},
    
    "field": ["deliveryTime", "productsCount", "productsWeight"]    
}


payload = {
    "deliveryTime": 12,
    "productsCount": 5,
    "productsWeight": 1
}

def post_response_json(name_field: str, value):
    data = payload.copy()
    data[name_field] = value
    client.post(config.settings.ENDPOINTS["delivery_broomstick"], data)


def check_success_response(
    name: str,
    host_cost: int,
    time_min: int=20,
    time_max: int=25,
    code: int=200,
    client_cost: int=0,
    PossibleToDeliver: bool=True):
    
    response_data = DeliveryResponse.model_validate(client.response_json)
    assert client.response.status_code == code
    assert response_data.name == name
    assert response_data.isItPossibleToDeliver == PossibleToDeliver
    assert response_data.hostDeliveryCost == host_cost
    assert response_data.toBeDeliveredTime.min == time_min
    assert response_data.toBeDeliveredTime.max == time_max
    assert response_data.clientDeliveryCost == client_cost
    DeliveryResponse.model_validate(client.response_json)
    
    
def check_error_response(code: int=400):
    assert client.response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert client.response.status_code == code
    assert client.response_json["code"] == code
    assert isinstance(client.response_json["message"], str)     
    
    
@pytest.mark.parametrize("productsCount", PAYLOAD_DATA["productsCount"]["positive"]["0-9"])
def test_correct_quantity_max9(productsCount):
    post_response_json(PRODUCTS_COUNT, productsCount)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=25, time_min=20, time_max=25)


@pytest.mark.parametrize("quantity", PAYLOAD_DATA["productsCount"]["positive"]["10-15"])
def test_correct_quantity_max15(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=40, time_min=20, time_max=25)
    
@pytest.mark.parametrize("quantity", PAYLOAD_DATA["productsCount"]["positive"]["16-30"])
def test_correct_quantity_16_30(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=40, time_min=20, time_max=25, client_cost=99)

    
@pytest.mark.parametrize("quantity", PAYLOAD_DATA["productsCount"]["negative"])
def test_negative_quantity(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_error_response()


@pytest.mark.parametrize("weight", PAYLOAD_DATA["productsWeight"]["positive"]["0-3"])
def test_correct_weight_max3(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=25, time_min=20, time_max=25) 

     
@pytest.mark.parametrize("weight", PAYLOAD_DATA["productsWeight"]["positive"]["3.1-6"])
def test_correct_weight_max3_6(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=40, time_min=20, time_max=25) 
    
@pytest.mark.parametrize("weight", PAYLOAD_DATA["productsWeight"]["positive"]["6.1-10"])
def test_correct_weight_max6_10(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=40, time_min=20, time_max=25, client_cost=99) 

     
@pytest.mark.parametrize("weight", PAYLOAD_DATA["productsWeight"]["negative"])
def test_negative_weight(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_error_response()


@pytest.mark.parametrize("delivery_time", PAYLOAD_DATA["deliveryTime"]["positive"])
def test_correct_delivery_time(delivery_time):
    post_response_json(DELIVERY_TIME, delivery_time)
    check_success_response(BROOMSTICK_DELIVERY, host_cost=25, time_min=20, time_max=25)

     
@pytest.mark.parametrize("delivery_time", PAYLOAD_DATA["deliveryTime"]["negative"])
def test_negative_delivery_time(delivery_time):
    post_response_json(DELIVERY_TIME, delivery_time)
    check_error_response()


@pytest.mark.parametrize("field", PAYLOAD_DATA["field"])
def test_negative_del_one_field(field):
    data = payload.copy()
    del data[field]
    client.post(config.settings.ENDPOINTS["delivery_broomstick"], data)
    check_error_response()
    
def test_negative_empty_body():
    data = payload.copy()
    del data["deliveryTime"]
    del data["productsCount"]
    del data["productsWeight"]
    client.post(config.settings.ENDPOINTS["delivery_broomstick"], data)
    check_error_response()