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
