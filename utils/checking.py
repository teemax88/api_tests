"""Методы проверки ответов на запросы"""
import json

from requests import Response


class Checking():
    """Метод для проверки статус кода"""

    def checking_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провал!!! Статус код = {response.status_code}"
        if response.status_code == status_code:
            print(f"Успешно!!! Статус код = {response.status_code}")

    """Метод для проверки наличия обязательных полей"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")