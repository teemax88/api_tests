import random
from utils.checking import Checking
from utils.http_methods import Http_method

URL = 'https://reqres.in/api/resource'
total_count = 0
count = 0


class Test_resource():

    def test_get_resource_list(self):
        global total_count, count
        print("Метод GET список всех ресурсов")
        result_list = Http_method.get(URL)  # получили весь список ресурсов

        total_count = int(result_list.json()['total'])  # взяли общее количество ресурсов и сохранили в переменную
        count = random.randint(1, total_count)  # выбрали рандомное число из имеющихся id ресурсов

        Checking.checking_status_code(result_list, 200)  # проверяем, что стаутс ответа == 200

    def test_get_resource(self):
        print("Метод GET для несуществующего русурса")
        result = Http_method.get(f"{URL}/{total_count + 1}")  # получаем ответ для несуществующего ресурса

        Checking.checking_status_code(result, 404)  # проверяем, что стаутс ответа == 404

    def test_get_unknown_resource(self):
        print(f"Метод GET для ресурса с ID = {count}")
        result_one_resource = Http_method.get(f"{URL}/{count}")  # Получаем информцию об одном ресурсе

        Checking.checking_status_code(result_one_resource, 200)

    def test_put_resource(self):
        print(f"Метод PUT изменение для ресурса с ID = {count}")
        result_update = Http_method.put_without_body(f"{URL}/{count}")

        Checking.checking_status_code(result_update, 200)

    def test_delete_resource(self):
        print(f"Метод DELETE удаление для ресурса с ID = {count}")
        result_delete = Http_method.delete(f"{URL}/{count}")

        Checking.checking_status_code(result_delete, 204)