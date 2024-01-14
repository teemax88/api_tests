import requests


class Http_method:
    @staticmethod  # позволяет нам не прописывать внутри функции self параметр, и не привязываться к классу
    def get(url: str, params: dict = None, **kwargs):
        # return requests.request("GET", url=url, **kwargs)
        print(requests.get(url, params, **kwargs))
        return requests.get(url, params, **kwargs)
        # return response

    @staticmethod
    def post(url: str, headers, data=None, **kwargs):
        return requests.request("POST", url=url, headers=headers, data=data, **kwargs)

    @staticmethod
    def put(url: str, **kwargs):
        return requests.request("PUT", url=url, **kwargs)

    @staticmethod
    def delete(url: str, **kwargs):
        return requests.request("DELETE", url=url, **kwargs)
