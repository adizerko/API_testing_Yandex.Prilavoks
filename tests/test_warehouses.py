import pytest
import config.settings
from utils.api_client import APIClient
from schemas.user_schema import Shop

client = APIClient()

@pytest.mark.parametrize("shop_name, expected_start, expected_end", config.settings.WAREHOUSES_DATA)
def test_get_warehouses(shop_name, expected_start, expected_end):
    client.get(config.settings.ENDPOINTS['get_warehouse'])
    shop_list = Shop.model_validate(client.response_json)

    matched = [shop for shop in shop_list.root if shop.name == shop_name]
    assert matched, f"Магазин '{shop_name}' не найден в ответе"
    
    shop = matched[0]
    assert shop.workingHours.start == expected_start, f"Неверное время начала у {shop.name}"
    assert shop.workingHours.end == expected_end, f"Неверное время окончания у {shop.name}"




    


