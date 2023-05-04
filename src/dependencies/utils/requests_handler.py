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
            self.url = "http://localhost:3000/"

    def push(self, url_postfix: str, data: dict):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(self.url + url_postfix, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            try:
                return response.json()["_id"]
            except KeyError:
                return response.json()["id"]
        else:
            print(response.status_code)
            print(response.request.body)
            exit(1)
