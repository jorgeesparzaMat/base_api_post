import json
import math
from datetime import datetime


class Log:
    def __init__(self, context, evento=""):
        """Crea objeto de log recibiendo contexto como parametro para la obtencion de datos"""
        self.code = ""
        self.error_message = ""
        self.error_technical = ""
        self.data_in = {}
        self.data_out = {}
        self.transaccion_id = ""
        self.cuenta_id = ""
        self.organizacion_id = ""
        self.ubicacion_id = ""
        self.request_id = ""
        self.effect = ""
        self.cuenta_tipo = ""
        self.ciclo = ""

        lambda_name = str(context.function_name)
        self.api = lambda_name.split("_")[0]
        self.recurso = lambda_name.split("_")[1]
        self.accion = lambda_name.split("_")[2]
        self.time_inicial = datetime.now()
        self.evento = evento

    def set_encabezado(self, j_input):
        """Genera log de los principales datos contenido en el log"""
        self.request_id = j_input.get("request_id", "")
        self.cuentaid = j_input["cuenta_id"]
        self.organizacion_id = j_input["organizacion_id"]
        self.cuenta_tipo = j_input["cuenta_tipo"]
        self.ubicacion_id = j_input.get("ubicacion_id", "")

    def set_error(self, code, error_message, error_technical):
        """Inserta parametros de log"""
        self.code = code
        self.error_message = error_message
        self.error_technical = error_technical

    def set_data_in(self, data_in):
        self.data_in = data_in

    def set_data_out(self, data_out):
        self.data_out = data_out

    def set_transaccion_id(self, transaccion_id):
        self.transaccion_id = transaccion_id

    def set_cuenta_id(self, cuenta_id):
        self.cuentaid = cuentaid

    def set_organizacion_id(self, organizacion_id):
        self.organizacion_id = organizacion_id

    def set_ubicacion_id(self, ubicacion_id):
        self.ubicacion_id = ubicacion_id

    def set_request_id(self, request_id):
        self.request_id = request_id

    def set_effect(self, effect):
        self.effect = effect

    def set_evento(self, evento):
        self.evento = evento

    def set_ciclo(self, ciclo):
        self.ciclo = ciclo

    def log(self):
        """Imprime log en newRelic"""
        try:
            j_log = {}

            self.time_final = datetime.now()
            self.tiempo_ejecucion = self.time_final - self.time_inicial

            j_log["type"] = "log"
            j_log["api"] = self.api
            j_log["recurso"] = self.recurso
            j_log["accion"] = self.accion
            j_log["evento"] = self.evento
            j_log["code"] = self.code
            j_log["error_message"] = self.error_message
            j_log["error_technical"] = self.error_technical
            j_log["data_in"] = self.data_in
            j_log["data_out"] = self.data_out
            j_log["transaccion_id"] = self.transaccion_id
            j_log["cuenta_id"] = self.cuenta_id
            j_log["organizacion_id"] = self.organizacion_id
            j_log["cuenta_tipo"] = self.cuenta_tipo
            j_log["ubicacion_id"] = self.ubicacion_id
            j_log["request_id"] = self.request_id
            j_log["effect"] = self.effect
            j_log["ciclo"] = self.ciclo
            j_log["time_inicial"] = self.time_inicial.strftime("%d-%m-%Y %H:%M:%S.%f")
            j_log["time_final"] = self.time_final.strftime("%d-%m-%Y %H:%M:%S.%f")
            j_log["tiempo_ejecucion"] = math.trunc(
                self.tiempo_ejecucion.total_seconds() * 1000
            )
            print(json.dumps(j_log))

        except Exception as e:
            pass
