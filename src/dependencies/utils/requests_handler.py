import json

import requests


class RequestsHandler:
    __instance = None

    @staticmethod
    def get_instance():
        if RequestsHandler.__instance is None:
            RequestsHandler()
        return RequestsHandler.__instance

    def __init__(self):
        if RequestsHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RequestsHandler.__instance = self
            self.url = "http://localhost:8080/"
            self.session = requests.Session()

    def push(self, url_postfix: str, data: dict):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = self.session.post(self.url + url_postfix, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            try:
                return response.json()["_id"]
            except KeyError:
                return response.json()["id"]
        else:
            print(response.status_code)
            print(response.json())
            exit(1)

    def patch(self, url_postfix: str, data: dict):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = self.session.patch(self.url + url_postfix, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            exit(1)
