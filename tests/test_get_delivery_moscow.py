import pytest
import config.settings
from utils.api_client import APIClient

client = APIClient()

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

response = {
    "name": "Доставка Москва",
    "isItPossibleToDeliver": True,
    "hostDeliveryCost": 45,
    "toBeDeliveredTime": {
        "min": 30,
        "max": 35
    },
    "clientDeliveryCost": 99

}
    
@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_pos_0_10"])
def test_correct_quantity_max10(quantity):
    data = payload.copy()
    data["productsCount"] = quantity
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.status_code == 200
    assert client.response_json["name"] == "Доставка Москва"
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == 30
    assert client.response_json["toBeDeliveredTime"]["min"] == 25    
    assert client.response_json["toBeDeliveredTime"]["max"] == 35
    assert client.response_json["clientDeliveryCost"] == 0


@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_pos_10_15"])
def test_correct_quantity_max15(quantity):
    data = payload.copy()
    data["productsCount"] = quantity
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 200
    assert client.response_json["name"] == "Доставка Москва"
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == 45
    assert client.response_json["toBeDeliveredTime"]["min"] == 30    
    assert client.response_json["toBeDeliveredTime"]["max"] == 35
    assert client.response_json["clientDeliveryCost"] == 0
    
@pytest.mark.parametrize("quantity", QUANTITY_DATA["quantity_neg"])
def test_negative_quantity(quantity):
    data = payload.copy()
    data["productsCount"] = quantity
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str)
    
@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_pos_0_3"])
def test_correct_weight_max3(weight):
    data = payload.copy()
    data["productsWeight"] = weight
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 200
    assert client.response_json["name"] == "Доставка Москва"
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == 25
    assert client.response_json["toBeDeliveredTime"]["min"] == 30    
    assert client.response_json["toBeDeliveredTime"]["max"] == 35
    assert client.response_json["clientDeliveryCost"] == 0
 
    
@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_pos_3.1_7"])
def test_correct_weight_max7(weight):
    data = payload.copy()
    data["productsWeight"] = weight
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 200
    assert client.response_json["name"] == "Доставка Москва"
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == 45
    assert client.response_json["toBeDeliveredTime"]["min"] == 30    
    assert client.response_json["toBeDeliveredTime"]["max"] == 35
    assert client.response_json["clientDeliveryCost"] == 0
     
@pytest.mark.parametrize("weight", QUANTITY_DATA["weight_neg"])
def test_negative_weight(weight):
    data = payload.copy()
    data["productsWeight"] = weight
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str)     

@pytest.mark.parametrize("delivery_time", QUANTITY_DATA["delivery_time_pos"])
def test_correct_delivery_time(delivery_time):
    data = payload.copy()
    data["deliveryTime"] = delivery_time
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 200
    assert client.response_json["name"] == "Доставка Москва"
    assert client.response_json["isItPossibleToDeliver"] == True
    assert client.response_json["hostDeliveryCost"] == 25
    assert client.response_json["toBeDeliveredTime"]["min"] == 30    
    assert client.response_json["toBeDeliveredTime"]["max"] == 35
    assert client.response_json["clientDeliveryCost"] == 0
     
@pytest.mark.parametrize("delivery_time", QUANTITY_DATA["delivery_time_neg"])
def test_negative_delivery_time(delivery_time):
    data = payload.copy()
    data["deliveryTime"] = delivery_time
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str) 
    
@pytest.mark.parametrize("field", QUANTITY_DATA["field"])
def test_negative(field):
    data = payload.copy()
    del data[field]
    client.post(config.settings.ENDPOINTS["delivery_Moscow"], data)
    
    assert client.response.headers["Content-Type"]
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert isinstance(client.response_json["message"], str) 
    
    
     