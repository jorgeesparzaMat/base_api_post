import json
import os
import sys


class OutputSinSeguridad:
    def __init__(self, ambiente):
        self.body = {}
        self.data = {}
        self.error = {}
        self.ambiente = ""
        self.status_code = ""
        self.user_message = ""
        self.technical_message = ""
        self.ambiente = ambiente.upper()

    def set_status_code(self, code, user_message, technical_message):
        self.status_code = code
        self.user_message = user_message
        self.technical_message = technical_message

    def set_ambiente(self, ambiente):
        self.ambiente = ambiente.upper()

    def set_data(self, data):
        self.data = data

    def set_request_id(self, request_id):
        self.request_id = request_id

    def carga(self):

        output = {}
        output["statusCode"] = self.status_code

        if (self.status_code != "200") and (self.ambiente != "PR"):
            self.error["technical_message"] = self.technical_message
            self.body["error"] = self.error

        self.body["data"] = self.data
        self.body["status_code"] = self.status_code
        self.body["user_message"] = self.user_message

        output["body"] = json.dumps(self.body)
        return output
