# from utils.api import Google_maps_api
# from utils.api import Reqres
from utils.checking import Checking
from requests import Response
from utils.http_methods import Http_method
from random import randint

endpoint = {
    'res': 'resource',
    'us': 'users'
}
num = randint(50, 100)

class Test_resource():
    def test_get_resource_list(self):
        print("Метод GET")
        result_get = Http_method.get(endpoint['res'])
        print(result_get.text)
        Checking.checking_status_code(result_get, 200)

    def test_get_unknown_resource(self):
        print("Метод GET")
        result_get = Http_method.get(f"{endpoint['res']}/{num}")
        print(result_get.text)
        Checking.checking_status_code(result_get, 404)

    def test_put_resource(self):
        print("Метод PUT")
        result_get = Http_method.get(f"{endpoint['res']}/{num}")
        print(result_get.text)
        Checking.checking_status_code(result_get, 404)