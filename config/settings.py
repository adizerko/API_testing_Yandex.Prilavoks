BASE_URL = "https://0d8f3d05-7dfd-471a-80d4-55c7236443a3.serverhub.praktikum-services.ru"

ENDPOINTS = {
    "get_warehouse": "/api/v1/warehouses",
    "add_user": "/api/v1/users",
    "get_delivery": "/api/v1/couriers",
    "delivery_Moscow": "/moscow-delivery/v1/calculate"
}

WAREHOUSES_DATA = [
    ("Имеется всё", 7, 23),
    ("Шведский дом", 8, 23),
    ("Чердак", 8, 21),
    ("Большой мир", 5, 20)
]

DELIVERY_DATA = [
    ("На метле уюта", 8, 22),
    ("Доставка Москва", 8, 22),
    ("Привезём быстро", 7, 21),
    ("Чух-чух и уже у вас", 6, 20)
]

USER_DATA = {
    "firstName": "Григорий",
    "email": "warmachi@ne1.ru",
    "phone": "+74441237887",
    "comment": "Ребёнок спит, не шумите",
    "address": "г. Москва, ул. Хохотушкина, д. 16"
}

PAYLOAD = { 
           "NAME_POSITIVE": ["Александра","Аа", "Ааа", "Аааааааааааааа", "Ааааааааааааааа",
                 "Alexandr", "Алекс-Алекс", "Алекс Алекс" ],
           
           "NAME_NEGATIVE":  ["А", "Аааааааааааааааа", "Ааааааааааааааааа",
                 "Аааааааааааааааааааа", "Alex@#!","嗨。", "Алекс123", ""],
           
           "PHONE_POSITIVE" : ["+7999999999", "+799999999", "+79999999999"],
           
           "PHONE_NEGATIVE" : ["+79999", "+7999999", "+79999999", "+79999999999999", "+799999999999", "+7999999999999", "+79FVSASgDD",
                  "+7%76#$%335", "+7925-95398", "+7838 98343", "79348765842", ""],
           
           "ADDRESS_POSITIVE" : ["Фрунзфрунзфрунзфрунзфрунз", "Фрунз", "фрунзф", "Фрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрун",
                    "Фрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунз", "Фрунунз-фрунзфру", "Фрунз,фрузф.", "Алекс Алекс", "Фрунзфрузф2132"],
           
           "ADDRESS_NEGATIVE" : ["Фрун", "Фр", "Фру", "Фрун", "Фрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунз",
                    "Фрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзф",
                    "Фрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфрунзфр",
                    "Frunzenskya", "Фрунзфрунз#@#", ""],
           
           "COMMENT_POSITIVE" : ["Аааааааааааа", "А", "Ааааааааааааааааааааааа", "Аааааааааааааааааааааааа", "Ааа-ааа", "Ааа,ааа.", "Ааа ааа", "Аааааа2132"],
           
           "COMMENT_NEGATIVE" : ["Аааааааааааааааааааааааааааааа", "Ааааааааааааааааааааааааа", "Аааааааааааааааааааааааааа", "Fasterplease", "Ааа$#@ааа"],
           
           "EMAIL_POSITIVE" : ["aaaaaaaaaa@yandex.ru", "a@r.u", "a@r.ru", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@yandex.ru",
                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@yandex.ru", "aaa-aa@yandex.ru", "aaa23232a@yandex.ru", ""],
           
           "EMAIL_NEGATIVE" : ["a@", "a@r", "a@r.", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@yandex.ru",
                  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@yandex.ru", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@yandex.ru",
                  "привет@яндекс.рф", "aa%;№aaa@yandex.ru", "aaaa a@yandex.ru", "aaa23232ayandex.ru", "aaaaa@yandexru", ]

}