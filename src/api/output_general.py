import json
import os
import sys

from generales.aes import Aes


class OutputGeneral:
    def __init__(self, ambiente):
        self.body = {}
        self.data = {}
        self.error = {}
        self.ambiente = ""
        self.status_code = ""
        self.user_message = ""
        self.technical_message = ""
        self.request_id = ""
        self.request_aes_key = ""
        self.ambiente = ambiente.upper()

    def set_status_code(self, code, user_message, technical_message):
        self.status_code = code
        self.user_message = user_message
        self.technical_message = technical_message

    def set_ambiente(self, ambiente):
        self.ambiente = ambiente.upper()

    def set_requests(self, j_input):
        self.request_id = j_input.get("request_id", "")
        self.request_key = j_input["request_key"]
        self.request_secret = j_input["request_secret"]

    def set_data(self, data):
        self.data = data

    def set_request_id(self, request_id):
        self.request_id = request_id

    def set_request_key(self, request_key):
        self.request_key = request_key

    def set_request_secret(self, request_secret):
        self.request_secret = request_secret

    def carga(self):

        respuesta_encrypt_body = {}
        respuesta_encrypt_body["body_encriptado"] = ""
        respuesta_encrypt_body["body_firma"] = ""

        output = {}

        # SET STATUS CODE DE API GATEWAY
        output["statusCode"] = self.status_code

        # GENERA DATA DE RESUESTA
        if self.status_code not in ("200", "206") and (self.ambiente != "PR"):
            self.error["technical_message"] = self.technical_message
            self.body["error"] = self.error

        if self.status_code in ("200", "206"):
            respuesta_encrypt_body = Aes.encrypt_body(
                bytes.fromhex(self.request_key),
                self.request_secret[0:16].encode("utf-8"),
                json.dumps(self.data),
            )

        self.body["request_id"] = self.request_id
        self.body["status_code"] = self.status_code
        self.body["body_encriptado"] = respuesta_encrypt_body["body_encriptado"]
        self.body["body_firma"] = respuesta_encrypt_body["body_firma"]

        output["body"] = json.dumps(self.body)
        return output
