import random
import time

import pytest

from utils.checking import Checking
from utils.http_methods import Http_method

URL = 'https://dev-rest.qform.io/ru/v3'

# email_name = "redtest"
email_url = "https://www.mailforspam.com/mail"


class Test_auth_reg():
    def test_register_user(self, register_data):
        print(register_data)
        response = Http_method.post(f"{URL}/user/register", register_data)  # Метод POST для регистрации пользователя
        # print(response.text)
        Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200

        email_page = Http_method.get(f'{email_url}/{register_data["username"]}')
        html_email_page = email_page.text.split()
        if 'QForm' in html_email_page:
            inbox_page = Http_method.get(f'{email_url}/{register_data["username"]}/1')
            html_inbox_page = inbox_page.text.split()
            for word in html_inbox_page:
                if word.startswith('https://'):
                    get_link = word.split('<')[0]

        confirm_email = Http_method.get(get_link)
        print(confirm_email.text)
        Checking.checking_status_code(confirm_email, 200)  # проверяем, что стаутс ответа == 200
        time.sleep(10)

    def test_auth_via_login(self, auth_data_via_login):
        response = Http_method.post(f"{URL}/auth", auth_data_via_login)  # Метод POST для регистрации пользователя
        print(response.text)
        # Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200
