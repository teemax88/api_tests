from utils.checking import Checking
from utils.http_methods import Http_method
from utils.http_methods import URL
from faker import Faker
import pytest


data = {
    "username": Faker().user_name(),
    "email": Faker().password(),
    "password": f"{Faker().user_name()}@reqres.in"
}


class Test_users():

    def test_register_user(self):
        global data
        print("Метод POST для создания пользователя")
        response = Http_method.post(f"{URL}/register", data)  # Регистрация нового пользователя

        print(response.json())

        Checking.checking_status_code(response, 200)  # проверяем, что стаутс ответа == 200


    # def test_get_resource(self):
    #     print(data)
        # print("Метод GET для несуществующего русурса")
        # result = Http_method.get(f"{URL}/{total_count + 1}")  # получаем ответ для несуществующего ресурса
        #
        # Checking.checking_status_code(result, 404)  # проверяем, что стаутс ответа == 404

    # @pytest.mark.skip
    # def test_get_unknown_resource(self):
    #     print(f"Метод GET для ресурса с ID = {count}")
    #     result_one_resource = Http_method.get(f"{URL}/{count}")  # Получаем информцию об одном ресурсе
    #
    #     Checking.checking_status_code(result_one_resource, 200)

    # @pytest.mark.skip
    # def test_put_resource(self):
    #     print(f"Метод PUT изменение для ресурса с ID = {count}")
    #     result_update = Http_method.put_without_body(f"{URL}/{count}")
    #
    #     Checking.checking_status_code(result_update, 200)
    #
    # @pytest.mark.skip
    # def test_delete_resource(self):
    #     print(f"Метод DELETE удаление для ресурса с ID = {count}")
    #     result_delete = Http_method.delete(f"{URL}/{count}")
    #
    #     Checking.checking_status_code(result_delete, 204)
