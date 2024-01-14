import pytest

from utils.data import MAIN_URL
from utils.http_methods import Http_method

# class Test_auth_reg():
#     def test_register_user(self, register_data):
#         "Метод POST для регистрации"
#         # response = Http_method.post(f"{URL}/user/register", register_data)
#         # Checking.checking_status_code(response, 200)
#
#         "Получение ссылки из почты"
#         email_page = Http_method.get(f'{MAIL_URL}/{register_data["username"]}')
#         html_email_page = email_page.text.split()
#         get_link = ""
#         if 'QForm' in html_email_page:
#             inbox_page = Http_method.get(f'{MAIL_URL}/{register_data["username"]}/1')
#             html_inbox_page = inbox_page.text.split()
#             for word in html_inbox_page:
#                 if word.startswith('https://'):
#                     link = word.split('<')
#                     get_link = link[0].split("?")[1]
#
#         "Запрос подтверждения почты напрямую в REST"
#         confirm_email = Http_method.get(f'{CONFIRM_URL}', get_link)

# print("**************--------------------------*********************")
# print(confirm_email.text)
# print("**************--------------------------*********************")
# Checking.checking_status_code(confirm_email, 200)

# def test_auth_via_login(self, auth_data_via_login):
#     response = Http_method.post(f"{URL}/auth", auth_data_via_login)  # Метод POST для регистрации пользователя
#     print(response.text)
# Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
