import hashlib
import hmac
import json
import os
import sys
from datetime import datetime
from random import randint

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from generales.fecha import Fecha
from generales.token import Token


class Aes:
    @staticmethod
    def decrypt_body(aes_key, aes_iv, body_encriptado, body_firma):

        respuesta = {}
        try:

            # SE ENCRIPTA BODY AES
            cipher = Cipher(
                algorithms.AES(aes_key), modes.CBC(aes_iv), backend=default_backend()
            )
            decryptor = cipher.decryptor()
            body_string = decryptor.update(body_encriptado)

            # SE FIRMA EL BODY ENCRIPTADO
            digest_maker = hmac.new(aes_key, b"", hashlib.sha256)
            digest_maker.update(body_encriptado)
            firma = digest_maker.hexdigest()

            if body_firma != firma:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Firma incorrecta"
                return respuesta

            # SE GENERA RESPUESTA

            respuesta["code"] = "OK"
            respuesta["body"] = json.loads(body_string.decode("utf-8"))
            return respuesta

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            err = "Archivo: {} - Linea:{} - Error: {} - {}".format(
                fname, exc_tb.tb_lineno, exc_obj, exc_type
            )

            respuesta["code"] = "NOK"
            respuesta["error_technical"] = err
            return respuesta

    @staticmethod
    def encrypt_body(aes_key, aes_iv, body_string):

        respuesta = {}
        try:

            largo_body_string = len(body_string)
            resto = largo_body_string % 32
            body_string = body_string.ljust(largo_body_string + 32 - resto, " ")
            body_bytes = body_string.encode("utf-8")

            # SE ENCRIPTA BODY AES
            cipher = Cipher(
                algorithms.AES(aes_key), modes.CBC(aes_iv), backend=default_backend()
            )
            encryptor = cipher.encryptor()
            body_encriptado = encryptor.update(body_bytes)

            # SE FIRMA EL BODY ENCRIPTADO
            digest_maker = hmac.new(aes_key, b"", hashlib.sha256)
            digest_maker.update(body_encriptado)
            firma = digest_maker.hexdigest()

            # SE GENERA RESPUESTA
            respuesta["code"] = "OK"
            respuesta["body_encriptado"] = body_encriptado.hex()
            respuesta["body_firma"] = firma
            return respuesta

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            err = "Archivo: {} - Linea:{} - Error: {} - {}".format(
                fname, exc_tb.tb_lineno, exc_obj, exc_type
            )

            respuesta["code"] = "NOK"
            respuesta["error_technical"] = err
            return respuesta
