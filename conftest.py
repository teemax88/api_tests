import json

import pytest
from faker import Faker


# username = Faker().user_name()
# email = f'{username}@mailforspam.com'
# password = Faker().password()

# username = "zxzxzxz"
# email = f'{username}@mailforspam.com'
# password = "zxzxzxz"

# @pytest.fixture
# def register_data():
#     data = {
#         "username": username,
#         "email": email,
#         "password": password,
#         "referer": {"host": "prod123.ru", "pathname": "/"},
#         "utm": {"utm_source": "vscode", "utm_medium": "click", "utm_campaign": "prosledit",
#                 "utm_content": "registration", "utm_term": "pishpish"}
#     }
# data = {
#     "username": "redtest",
#     "email": "redtest@mailforspam.com",
#     "password": "redtest",
#     "country_id": "1",
#     "language_locale": "ru",
#     "referer": {"host": "prod123.ru", "pathname": "/"},
#     "utm": {"utm_source": "vscode", "utm_medium": "click", "utm_campaign": "prosledit",
#             "utm_content": "registration", "utm_term": "pishpish"}
# }
# return data


# @pytest.fixture
# def auth_data_via_login(register_data):
#     data = {"username": register_data["username"],
#             "password": register_data["password"]
#             }
#     # data = {'username': 'google2', 'password': '123456qp'}
#     return data
#
#
# @pytest.fixture
# def auth_data_via_email(register_data):
#     data = {"email": register_data["email"],
#             "password": register_data["password"]
#             }
# data = {
#     "username": "nerickson",
#     "email": "reedanthony@mailforspam.com",
#     "password": "(5!HUT6ucH"
# }
# return data


@pytest.fixture
def user_data():
    payload = json.dumps({
        "id": 111111111111,
        "username": "jim",
        "firstName": "carrey",
        "lastName": "test",
        "email": "jimm@mail.ru",
        "password": "jim123456",
        "phone": "123456789",
        "userStatus": 1
    })
    return payload
