import pytest
import config.settings
from utils.api_client import APIClient, CheckStatus
from schemas.user_schema import Shop
import allure


client = APIClient()
check_status = CheckStatus()

message_empty = "Не все необходимые параметры были переданы"
message_uncorrect = {
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
            assert client.response_json["message"] == expected_msg



def test_correct_add_user_max_():
    client.post((config.settings.ENDPOINTS["add_user"]),
                config.settings.USER_DATA)
    
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("name", config.settings.PAYLOAD["NAME_POSITIVE"], ids=str)
def test_positive_name_add_user(name):
    data = config.settings.USER_DATA.copy()
    data["firstName"] = name
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 201
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("name", config.settings.PAYLOAD["NAME_NEGATIVE"], ids=str)
def test_negative_name_add_user(name):
    data = config.settings.USER_DATA.copy()
    data["firstName"] = name
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    
    if data["firstName"] == "":
        assert client.response_json["message"] == "Не все необходимые параметры были переданы"
    else:   
        assert client.response_json["message"] == "Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов"
 
@pytest.mark.parametrize("phone", config.settings.PAYLOAD["PHONE_POSITIVE"], ids=str)
def test_positive_phone_add_user(phone):
    data = config.settings.USER_DATA.copy()
    data["phone"] = phone
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 201
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("phone", config.settings.PAYLOAD["PHONE_NEGATIVE"], ids=str)
def test_negative_phone_add_user(phone):
    data = config.settings.USER_DATA.copy()
    data["phone"] = phone
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    
    if data["phone"] == "":
        assert client.response_json["message"] == "Не все необходимые параметры были переданы"
    else:
        assert client.response_json["message"] == "Телефонный номер пользователя введен некорреткно. Номер может содержать только цифры и знак +"
        
@pytest.mark.parametrize("address", config.settings.PAYLOAD["ADDRESS_POSITIVE"], ids=str)
def test_positive_addres_add_user(address):
    data = config.settings.USER_DATA.copy()
    data["address"] = address
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 201
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("address", config.settings.PAYLOAD["ADDRESS_NEGATIVE"], ids=str)
def test_negative_address_add_user(address):
    data = config.settings.USER_DATA.copy()
    data["address"] = address
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    
    if data["address"] == "":
        assert client.response_json["message"] == "Не все необходимые параметры были переданы"
    else:
        assert client.response_json["message"] == "Адресс введен некорректно. Адрес может содержать только русские буквы, цифры и знаки препинания, длина адреса не должна быть менее 5 и более 50 символов"
    
@pytest.mark.parametrize("comment", config.settings.PAYLOAD["COMMENT_POSITIVE"], ids=str)
def test_positive_comment_add_user(comment):
    data = config.settings.USER_DATA.copy()
    data["comment"] = comment
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 201
    assert client.response_json["authToken"]
    
@pytest.mark.parametrize("comment", config.settings.PAYLOAD["COMMENT_NEGATIVE"], ids=str)
def test_negative_comment_add_user(comment):
    data = config.settings.USER_DATA.copy()
    data["comment"] = comment
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    
    if data["comment"] == "":
        assert client.response_json["message"] == "Не все необходимые параметры были переданы"
    else:
        assert client.response_json["message"] == "Комментарий пользователя. Комментарий может содержать только русские символы и знаки препинания, длина комментария не должгна быть более 24 символов"
        
@pytest.mark.parametrize("email", config.settings.PAYLOAD["EMAIL_POSITIVE"], ids=str)
def test_positive_email_add_user(email):
    data = config.settings.USER_DATA.copy()
    data["email"] = email
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 201
    assert client.response_json["authToken"]     
    
@pytest.mark.parametrize("email", config.settings.PAYLOAD["EMAIL_NEGATIVE"], ids=str)
def test_negative_email_add_user(email):
    data = config.settings.USER_DATA.copy()
    data["email"] = email
    client.post((config.settings.ENDPOINTS["add_user"]), data)
    
    assert client.response.status_code == 400
    assert client.response_json["code"] == 400
    assert client.response_json["message"] == "Адрес электронной почты пользователя введен некорректно. Адрес может содержать только латинские символы,символы .-@, длина должна быть не менее 5 и не более 50 символов" 