import pytest


# import requests

def test_example():
    assert isinstance('hello', str)


"""****************************//////////////////////////////************************"""

# import json
# from utils.data import MAIN_URL
# from utils.http_methods import Http_method
# from utils.checking import Checking
#
# headers = {
#     'Content-Type': 'application/json'
# }
#
#
# def test_create_user(user_data):
#     response = Http_method.post(url=MAIN_URL + '/user', headers=headers, data=user_data)
#     print(response.text)
#     print(f'response === {response.content}')
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_create_with_array(user_array):
#     response = Http_method.post(url=MAIN_URL + '/user/createWithArray', headers=headers, data=user_array)
#     print(f'response ====', response.text)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_create_with_list(user_list):
#     response = Http_method.post(url=MAIN_URL + '/user/createWithList', headers=headers, data=user_list)
#     print(f'response====', response.text)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# def test_get_user(user_data):
#     data = json.loads(user_data)
#
#     response = Http_method.get(url=MAIN_URL + '/user/' + data["username"], headers=headers)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_login_user(user_data):
#     try:
#         data = json.loads(user_data)
#     except json.JSONDecodeError:
#         raise ValueError("Ошибка в формате user_data")
#     payload = {"username": data["username"], "password": data["password"]}
#
#     response = Http_method.get(url=MAIN_URL + '/user/login', params=payload, headers=headers)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_update_user(user_data, new_user_data):
#     data = json.loads(user_data)
#
#     response = Http_method.put(url=MAIN_URL + '/user/' + data["username"], data=new_user_data, headers=headers)
#     print(f'response === {response.content}')
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_get2_user(user_data, new_user_data):
#     data = json.loads(user_data)
#     new_data = json.loads(new_user_data)
#
#     response = Http_method.get(url=MAIN_URL + '/user/' + data["username"], headers=headers)
#     print(f'response data === {response.content}')
#     # Checking.checking_status_code(response, 404)  # проверяем, что стаутс ответа == 404
#
#     response = Http_method.get(url=MAIN_URL + '/user/' + new_data["username"], headers=headers)
#     print(f'response new data === {response.content}')
#     # Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#
#
# @pytest.mark.skip
# def test_logout_user():
#     response = Http_method.get(url=MAIN_URL + '/user/logout', headers=headers)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
#     print(f'response === {response.content}')
#
#
# @pytest.mark.skip
# def test_delete_user(user_data, new_user_data):
#     try:
#         data = json.loads(user_data)
#         new_data = json.loads(new_user_data)
#     except json.JSONDecodeError:
#         raise ValueError("Ошибка в формате user_data")
#
#     response = Http_method.delete(url=MAIN_URL + '/user/' + data["username"], headers=headers)
#     Checking.checking_status_code(response, 404)  # проверяем, что стаутс ответа == 404
#
#     response = Http_method.delete(url=MAIN_URL + '/user/' + new_data["username"], headers=headers)
#     Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


# def to_json(self) -> str:
#     """Returns the JSON representation of the model using alias"""
#     # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
#     return json.dumps(self.to_dict())
#
# @classmethod
# def from_json(cls, json_str: str) -> Self:
#     """Create an instance of AttachmentGet from a JSON string"""
#     return cls.from_dict(json.loads(json_str))


"""****************************//////////////////////////////************************"""

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
