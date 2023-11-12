import requests


class Http_method:
    @staticmethod  # позволяет нам не прописывать внутри функции self параметр, и не привязываться к классу
    def get(url, **kwargs):
        return requests.request("GET", url, **kwargs)
        # return response

    @staticmethod
    def post(url: str, payload: dict):
        return requests.request("POST", url, data=payload)

    @staticmethod
    def put(url, **kwargs):
        return requests.request("PUT", url, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return requests.request("DELETE", url=url, **kwargs)
