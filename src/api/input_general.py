import json
import os
import sys

from generales.aes import Aes


class InputGeneral:
    @staticmethod
    def carga(input):

        respuesta = {}

        try:
            ################################################
            # SE COPIA LA VARIABLE DE ENTRADA
            ################################################
            j_input = input.copy()

            ################################################
            # SE CARGAN PARAMETROS DE ENTRADA
            ################################################

            # requestContext
            request_context = {}
            request_context = j_input["requestContext"]

            # authorizer
            authorizer = {}
            authorizer = request_context["authorizer"]

            # principalId
            principal_id = {}
            principal_id_string = authorizer["principalId"]
            principal_id = json.loads(principal_id_string)

            # request_key
            if "request_key" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin request_key"
                return respuesta
            request_key = principal_id["request_key"]

            # usuario_data
            if "usuario_data" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin usuario_data"
                return respuesta
            usuario_data = principal_id["usuario_data"]

            # cuenta_id
            if "cuenta_id" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin cuenta_id"
                return respuesta
            cuenta_id = principal_id["cuenta_id"]

            # ubicacion_id
            if "ubicacion_id" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin ubicacion_id"
                return respuesta
            ubicacion_id = principal_id["ubicacion_id"]

            # organizacion_id
            if "organizacion_id" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin organizacion_id"
                return respuesta
            organizacion_id = principal_id["organizacion_id"]

            # cuenta_tipo
            if "cuenta_tipo" not in principal_id:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin cuenta_tipo"
                return respuesta
            cuenta_tipo = principal_id["cuenta_tipo"]

            # headers
            headers = j_input["headers"]

            # requestid
            if "requestid" not in headers:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin requestid"
                return respuesta
            request_id = headers["requestid"]

            # requestSecret
            if "requestsecret" not in headers:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin requestSecret"
                return respuesta
            request_secret = headers["requestsecret"]

            # X-Forwarded-For
            if "X-Forwarded-For" not in headers:
                respuesta["code"] = "NOK"
                respuesta["error_technical"] = "Request sin X-Forwarded-For"
                return respuesta
            x_forwarded_for = headers["X-Forwarded-For"]

            # query string parameters
            if "queryStringParameters" in j_input:
                respuesta["query_string_parameters"] = j_input["queryStringParameters"]

            # pathParameters
            if "pathParameters" in j_input and j_input["pathParameters"]:
                respuesta["path_parameters"] = j_input["pathParameters"]

            # body
            if j_input["httpMethod"] != "GET":
                body = {}
                body_string = j_input["body"]
                body = json.loads(body_string)
                body_encriptado = body["body_encriptado"]
                body_firma = body["body_firma"]
                ################################################
                # SE DESENCRIPTA BODY
                ################################################
                respuesta_decrypt_body = Aes.decrypt_body(
                    bytes.fromhex(request_key),
                    request_secret[16:32].encode("utf-8"),
                    bytes.fromhex(body_encriptado),
                    body_firma,
                )
                if respuesta_decrypt_body["code"] != "OK":
                    respuesta["code"] = "NOK"
                    respuesta["error_technical"] = respuesta_decrypt_body[
                        "error_technical"
                    ]
                    return respuesta
                body = respuesta_decrypt_body["body"]
            else:
                body = {}

            ################################################
            # SE GENERA RESPUESTA
            ################################################
            respuesta["stage"] = request_context["stage"].upper()
            respuesta["ambiente"] = respuesta["stage"].upper()
            respuesta["ip_origen"] = x_forwarded_for
            respuesta["request_id"] = request_id
            respuesta["cuenta_id"] = cuenta_id
            respuesta["ubicacion_id"] = ubicacion_id
            respuesta["usuario_data"] = usuario_data
            respuesta["request_key"] = request_key
            respuesta["request_secret"] = request_secret
            respuesta["organizacion_id"] = organizacion_id
            respuesta["cuenta_tipo"] = cuenta_tipo
            respuesta["body"] = body

            # respuesta
            respuesta["code"] = "OK"
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
