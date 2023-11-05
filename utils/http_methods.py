import requests
from utils.logger import Logger
import allure

"""Список HTTP методов"""


class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""
    payload = {}

    @staticmethod  # позволяет нам не прописывать внутри функции self параметр, и не привязываться к классу
    def get(url: str):
        response = requests.get(url=url,  params=Http_method.payload, headers=Http_method.headers, cookies=Http_method.cookie)
        return response

    @staticmethod
    def post(url: str, body: dict):
        response = requests.post(url=url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return response

    @staticmethod
    def put(url: str, body: dict):
        response = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return response

    @staticmethod
    def put_without_body(url: str):
        response = requests.put(url=url, headers=Http_method.headers, cookies=Http_method.cookie)
        return response

    @staticmethod
    def delete(url: str):
        response = requests.delete(url=url, headers=Http_method.headers, cookies=Http_method.cookie)
        return response
