import pytest
import config.settings
from utils.api_client import APIClient


client = APIClient()


MOSCOW_DELIVERY = "Доставка Москва"
DELIVERY_TIME = "deliveryTime"
PRODUCTS_COUNT = "productsCount"
PRODUCTS_WEIGHT = "productsWeight"
QUANTITY_DATA = {
    "quantity_pos_0_10": [0, 1, 5, 9, 10],
    "quantity_pos_10_15": [11, 12, 13, 14, 15],
    "quantity_neg": [-1, -5, "" , 123423423, "sd", "#@", "4-3", "4 4", -15, 12.0],
    "weight_pos_0_3": [0, 0.1, 0.2, 1, 2, 2.9, 3, 3.0],
    "weight_pos_3.1_7": [3.1, 3.2, 4, 5, 5.5, 6.9, 7, 7.0],
    "weight_neg": ["sd", "#@", "4-3", "4 4", -15, 12341241214241, -0.1, ""],
    "delivery_time_pos": [8,9,15,21,22],
    "delivery_time_neg": [6,7,23,24,25,44, 343444444, -5, 15.5, "sd", "#@", "4-3", "4 4", ""],
    "field": ["deliveryTime", "productsCount", "productsWeight"]
    }

payload = {
    "deliveryTime": 12,
    "productsCount": 8,
    "productsWeight": 2
}

def post_response_json(name_field, value):
    data = payload.copy()
    data[name_field] = value
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)


def check_success_response(name, host_cost, time_min=30, time_max=35, code=200, client_cost=0, PossibleToDeliver=True):
    assert client.response.status_code == code
    assert client.response_json["name"] == name
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == host_cost
    assert client.response_json["toBeDeliveredTime"]["min"] == time_min  
    assert client.response_json["toBeDeliveredTime"]["max"] == time_max
    assert client.response_json["clientDeliveryCost"] == client_cost
    
    
def check_error_response():
    assert client.response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str)     
    
    
@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_pos_0_10"])
def test_correct_quantity_max10(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_success_response(config.settings.MOSCOW_DELIVERY, 25)


@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_pos_10_15"])
def test_correct_quantity_max15(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_success_response(MOSCOW_DELIVERY, 45)
    
    
@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_neg"])
def test_negative_quantity(quantity):
    post_response_json(PRODUCTS_COUNT, quantity)
    check_error_response()


@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_pos_0_3"])
def test_correct_weight_max3(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_success_response(MOSCOW_DELIVERY, 25) 
 
     
@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_pos_3.1_7"])
def test_correct_weight_max7(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_success_response(MOSCOW_DELIVERY, 45) 
   
     
@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_neg"])
def test_negative_weight(weight):
    post_response_json(PRODUCTS_WEIGHT, weight)
    check_error_response()


@pytest.mark.parametrize("delivery_time", QUANTITY_DATA["delivery_time_pos"])
def test_correct_delivery_time(delivery_time):
    post_response_json(DELIVERY_TIME, delivery_time)
    check_success_response(MOSCOW_DELIVERY, 25)
  
     
@pytest.mark.parametrize("delivery_time", QUANTITY_DATA["delivery_time_neg"])
def test_negative_delivery_time(delivery_time):
    post_response_json(DELIVERY_TIME, delivery_time)
    check_error_response()


@pytest.mark.parametrize("field", QUANTITY_DATA["field"])
def test_negative(field):
    data = payload.copy()
    del data[field]
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str) 
    
