import json
import os
import sys

from api.input_general import InputGeneral
from api.output_general import OutputGeneral
from aws.dynamo_db import DynamoDb
from generales.log import Log
from generales.salida_controlada import SalidaControlada
from schema.schema_input import SchemaInput

# SE LEEN VARIABLES DE ENTORNO
AMBIENTE = os.environ["ambiente"].upper()

# SE CREA RESOURCE DE DYNAMODB
resource_dynamo_db = DynamoDb.resource_custom()

# SE CREA CLIENT DE DYNAMODB
client_dynamo_db = DynamoDb.client_custom()

################################################
# SE DEFINEN LAS TABLAS
################################################
TABLA_NOMBRETABLA = "NOMBRETABLA"


def lambda_handler(event, context):

    ################################################
    # SE IMPRIME REQUEST SI AMBIENTE = DE
    ################################################
    if AMBIENTE == "DE":
        print(json.dumps(event))

    ################################################
    # SE CONFIGURA EL LOG
    ################################################
    log = Log(context)

    ################################################
    # SE DECLARA LA VARIABLE DE SALIDA
    ################################################
    data = {}
    j_output = OutputGeneral(AMBIENTE)

    try:
        ################################################
        # SE CARGA LA VARIABLE DE ENTRADA
        ################################################
        j_input = InputGeneral.carga(event)
        if j_input["code"] != "OK":
            raise SalidaControlada(
                "400",
                "Error al cargar datos de entrada",
                j_input["error_technical"],
            )

        ################################################
        # SE CARGA EL LOG
        ################################################
        log.set_encabezado(j_input)

        ################################################
        # SE CARGA LA VARIABLE DE SALIDA
        ################################################
        j_output.set_requests(j_input)

        ###############################################################################################
        ###############################################################################################
        ##############################################################################################
        ###############################################################################################
        ###############################################################################################
        ################################################
        # VALIDA SCHEMA
        ################################################
        respuesta_validacion_esquema = {}
        respuesta_validacion_esquema = SchemaInput.validar(j_input["body"])

        if respuesta_validacion_esquema["code"] == "NOK":
            raise SalidaControlada(
                "400",
                "Solicitud incorrecta: esquema invalido.",
                respuesta_validacion_esquema["error_technical"],
            )

        # CARGAMOS BODY DE INPUT EN VARIABLE
        item = j_input["body"]
        ###############################################################################################
        ###############################################################################################
        ###############################################################################################
        ###############################################################################################
        j_output.set_data(data)
        raise SalidaControlada(
            "200",
            "OK",
            "Datos cargados correctamente",
        )
    except SalidaControlada as x:
        log.set_error(x.codigo_error, x.user_message, x.technical_message)
        j_output.set_status_code(x.codigo_error, x.user_message, x.technical_message)

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        err = "Archivo: {} - Linea:{} - Error: {} - {}".format(
            fname, exc_tb.tb_lineno, exc_obj, exc_type
        )
        j_output.set_status_code("500", "Error en aplicacion", err)
        log.set_error("500", "Error Exception Principal", err)

    ########################################################
    # LOG Y RESULT
    ########################################################
    log.log()
    result = {}
    result = j_output.carga()
    print(json.dumps(result))
    return result
