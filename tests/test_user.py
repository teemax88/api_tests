import json

import pytest

from utils.data import MAIN_URL
from utils.http_methods import Http_method
from utils.checking import Checking

headers = {
    'Content-Type': 'application/json'
}


@pytest.mark.skip
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
    print(f'response ====', response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


@pytest.mark.skip
def test_login_user(user_data):
    data = json.loads(user_data)
    payload = {"username": data["username"], "password": data["password"]}

    response = Http_method.get(url=MAIN_URL + '/user/login', params=payload, headers=headers)
    print(f'response ====', response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


"///////////////////////"
def test_update_user(user_data):
    data = json.loads(user_data)
    payload = {"username": data["username"], "password": data["password"]}

    response = Http_method.get(url=MAIN_URL + '/user/' + data["username"], params=payload, headers=headers)
    print(f'response ====', response.text)
    Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200