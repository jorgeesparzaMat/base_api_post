import json
import os
import sys


class InputSinSeguridad:
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

            # headers
            headers = j_input["headers"]

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

            # httpMethod
            metodo = ""
            metodo = request_context["httpMethod"]

            # body
            if metodo != "GET":
                body = {}
                body_string = j_input["body"]
                body = json.loads(body_string)

            else:
                body = {}

            ################################################
            # SE GENERA RESPUESTA
            ################################################
            respuesta["stage"] = request_context["stage"].upper()
            respuesta["ambiente"] = respuesta["stage"].upper()
            respuesta["ip_origen"] = x_forwarded_for
            respuesta["headers"] = headers
            respuesta["metodo"] = metodo
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
