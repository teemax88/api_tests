import random

import pytest

from utils.checking import Checking
from utils.http_methods import Http_method, URL


class Test_auth_reg():
    # def test_register_user(self, register_data):
    #     response = Http_method.post(f"{URL}/user/register", register_data)  # Метод POST для регистрации пользователя
    #     print(response.json())
    #     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200

    def test_auth_via_login(self, auth_data):
        data = {"username": auth_data["username"],
                "password": auth_data["password"]
                }

        response = Http_method.post(f"{URL}/auth", data)  # Метод POST для регистрации пользователя
        print(f"Это ответ ----- {response.json()}")
        Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200

    # def test_get_resource(self):
    #     print("Метод GET для несуществующего русурса")
    #     result = Http_method.get(f"{URL}/resource/{total_count + 1}")  # получаем ответ для несуществующего ресурса
    #
    #     Checking.checking_status_code(result, 404)  # проверяем, что стаутс ответа == 404
    #
    # def test_get_unknown_resource(self):
    #     print(f"Метод GET для ресурса с ID = {count}")
    #     result_one_resource = Http_method.get(f"{URL}/resource/{count}")  # Получаем информцию об одном ресурсе
    #
    #     Checking.checking_status_code(result_one_resource, 200)
    #
    # def test_put_resource(self):
    #     print(f"Метод PUT изменение для ресурса с ID = {count}")
    #     result_update = Http_method.put_without_body(f"{URL}/resource/{count}")
    #
    #     Checking.checking_status_code(result_update, 200)
    #
    # def test_delete_resource(self):
    #     print(f"Метод DELETE удаление для ресурса с ID = {count}")
    #     result_delete = Http_method.delete(f"{URL}/resource/{count}")
    #
    #     Checking.checking_status_code(result_delete, 204)
