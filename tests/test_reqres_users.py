from utils.api import Google_maps_api
from utils.checking import Checking
from requests import Response

endpoint = {
    'res': 'resource',
    'us': 'users'
}


class Test_users():

    def test_create_new_place(self):
        pass
    #     print("Метод GET")
    #     result_get: Response = Google_maps_api.get_data(endpoint['res'])
    #     Checking.checking_status_code(result_get, 200)
    # Checking.check_json_token(result_get,
    #                           ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
    #                            'language'])
    # Checking.check_json_value(result_get, "name", "Frontline house")
