import json

import pytest

from utils.data import MAIN_URL
from utils.http_methods import Http_method
from utils.checking import Checking

headers = {
    'Content-Type': 'application/json'
}


def test_create_user(user_data):
    response = Http_method.post(url=MAIN_URL + '/user', headers=headers, data=user_data)
    print(response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_create_with_array(user_array):
    response = Http_method.post(url=MAIN_URL + '/user/createWithArray', headers=headers, data=user_array)
    print(f'response ====', response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_create_with_list(user_list):
    response = Http_method.post(url=MAIN_URL + '/user/createWithList', headers=headers, data=user_list)
    print(f'response====', response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_get_user(user_data):
    data = json.loads(user_data)

    response = Http_method.get(url=MAIN_URL + '/user/' + data["username"], headers=headers)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_login_user(user_data):
    try:
        data = json.loads(user_data)
    except json.JSONDecodeError:
        raise ValueError("Ошибка в формате user_data")
    payload = {"username": data["username"], "password": data["password"]}

    response = Http_method.get(url=MAIN_URL + '/user/login', params=payload, headers=headers)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


# import requests
# import json
#
#
# def test_login_user(user_data):
#     try:
#         data = json.loads(user_data)
#         username = data.get("username")
#         password = data.get("password")
#         if not username or not password:
#             raise ValueError("Отсутствуют имя пользователя или пароль")
#     except json.JSONDecodeError:
#         raise ValueError("Ошибка в формате user_data")
#
#     payload = {"username": username, "password": password}
#
#     try:
#         response = requests.get(url=MAIN_URL + '/user/login', params=payload, headers=headers)
#     except requests.RequestException as e:
#         raise ConnectionError(f"Ошибка соединения: {e}")
#
#     # Проверка статуса ответа
#     Checking.checking_status_code(response, 200)  # Проверяем, что статус ответа == 200
#
#     # Дополнительные проверки могут быть добавлены здесь
#     # Например, проверка содержимого ответа
#
#
# test_login_user(user_data)


def test_update_user(user_data, new_user_data):
    data = json.loads(user_data)

    response = Http_method.put(url=MAIN_URL + '/user/' + data["username"], data=new_user_data, headers=headers)
    print(f'response === {response.content}')
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_logot_user():
    response = Http_method.get(url=MAIN_URL + '/user/logout', headers=headers)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
    print(f'response === {response.content}')


def test_delete_user(user_data, new_user_data):
    try:
        data = json.loads(user_data)
        new_data = json.loads(new_user_data)
    except json.JSONDecodeError:
        raise ValueError("Ошибка в формате user_data")

    response = Http_method.delete(url=MAIN_URL + '/user/' + data["username"], headers=headers)
    Checking.checking_status_code(response, 404)  # проверяем, что стаутс ответа == 404

    response = Http_method.delete(url=MAIN_URL + '/user/' + new_data["username"], headers=headers)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
