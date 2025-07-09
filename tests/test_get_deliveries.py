import pytest
import config.settings
from utils.api_client import APIClient
from schemas.user_schema import Shop

client = APIClient()

@pytest.mark.parametrize("delivery_name, expected_start, expected_end", config.settings.DELIVERY_DATA)
def test_get_list_delivery(delivery_name, expected_start, expected_end):
    client.get(config.settings.ENDPOINTS['get_delivery'])
    delivery_list = Shop.model_validate(client.response_json)

    matched = [delivery for delivery in delivery_list.root if delivery.name == delivery_name]
    assert matched, f"Магазин '{delivery_name}' не найден в ответе"
    print(matched)
    delivery = matched[0]
    assert delivery.workingHours.start == expected_start, f"Неверное время начала у {delivery.name}"
    assert delivery.workingHours.end == expected_end, f"Неверное время окончания у {delivery.name}"

