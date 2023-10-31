import json

from utils.api import Google_maps_api
from utils.checking import Checking
from requests import Response

"""Создание, изменение и удаление новой локации"""


class Test_create_place():
    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')  # Просим вернуть значение ключа place_id

        Checking.checking_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))

        print("Метод GET after POST")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.checking_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        # token = json.loads(result_get.text)
        # print(list(token))

        print("Метод PUT")
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Checking.checking_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])

        print("Метод GET after PUT")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.checking_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("Метод DELETE")
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Checking.checking_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])

        print("Метод GET after DELETE")
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Checking.checking_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
