import pytest
import config.settings
from utils.api_client import APIClient
from schemas.user_schema import Shop
import allure

client = APIClient()

message_uncorrect = {
                    "empty": "Не все необходимые параметры были переданы",
                    "firstName": "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов",
                    "phone": "Телефонный номер пользователя введен некорреткно. Номер может содержать только цифры и знак +",
                    "address":"Адресс введен некорректно. Адрес может содержать только русские буквы, цифры и знаки препинания, длина адреса не должна быть менее 5 и более 50 символов",
                    "comment":"Комментарий пользователя. Комментарий может содержать только русские символы и знаки препинания, длина комментария не должгна быть более 24 символов",
                    "email":"Адрес электронной почты пользователя введен некорректно. Адрес может содержать только латинские символы,символы .-@, длина должна быть не менее 5 и не более 50 символов" 
                        }

    
def send_and_assert(field, value, expected_code=201, expected_msg=None):
    data = config.settings.USER_DATA.copy()
    data[field] = value
    client.post(config.settings.ENDPOINTS["add_user"], data)
    
    assert client.response.status_code == expected_code

    if expected_code == 201:
        assert "authToken" in client.response_json
    else:
        assert client.response_json["code"] == expected_code
        if expected_msg:
            if not value:
                assert client.response_json["message"] == message_uncorrect["empty"]
            else:
                assert client.response_json["message"] == expected_msg

def test_correct_add_user_max_():
    client.post((config.settings.ENDPOINTS["add_user"]),
                config.settings.USER_DATA)
    
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("name", config.settings.PAYLOAD["NAME_POSITIVE"], ids=str)
def test_positive_name_add_user(name):
    send_and_assert("name", name, 201)
    
@pytest.mark.parametrize("name", config.settings.PAYLOAD["NAME_NEGATIVE"], ids=str)
def test_negative_name_add_user(name):
    send_and_assert("firstName", name, 400, message_uncorrect["firstName"])

@pytest.mark.parametrize("phone", config.settings.PAYLOAD["PHONE_POSITIVE"], ids=str)
def test_positive_phone_add_user(phone):
    send_and_assert("phone", phone, 201)
    
@pytest.mark.parametrize("phone", config.settings.PAYLOAD["PHONE_NEGATIVE"], ids=str)
def test_negative_phone_add_user(phone):
    send_and_assert("phone", phone, 400, message_uncorrect["phone"])
        
@pytest.mark.parametrize("address", config.settings.PAYLOAD["ADDRESS_POSITIVE"], ids=str)
def test_positive_addres_add_user(address):
    send_and_assert("address", address, 201)
    
@pytest.mark.parametrize("address", config.settings.PAYLOAD["ADDRESS_NEGATIVE"], ids=str)
def test_negative_address_add_user(address):
    send_and_assert("address", address, 400, message_uncorrect["address"])

@pytest.mark.parametrize("comment", config.settings.PAYLOAD["COMMENT_POSITIVE"], ids=str)
def test_positive_comment_add_user(comment):
    send_and_assert("cooment", comment, 201)
    
@pytest.mark.parametrize("comment", config.settings.PAYLOAD["COMMENT_NEGATIVE"], ids=str)
def test_negative_comment_add_user(comment):
    send_and_assert("comment", comment, 400, message_uncorrect["comment"])

@pytest.mark.parametrize("email", config.settings.PAYLOAD["EMAIL_POSITIVE"], ids=str)
def test_positive_email_add_user(email):
    send_and_assert("email", email, 201)   
    
@pytest.mark.parametrize("email", config.settings.PAYLOAD["EMAIL_NEGATIVE"], ids=str)
def test_negative_email_add_user(email):
    send_and_assert("email", email, 400, message_uncorrect["email"] )