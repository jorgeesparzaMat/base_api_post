import json
import os
import sys

from jsonschema import validate


class SchemaInput:
    @staticmethod
    def validar(j_input):

        respuesta = {}

        try:
            # SCHEMA
            schema = {
                "type": "object",
                "properties": {
                    # VARIABLES OBLIGATORIAS
                    "param1": {"type": "string", "enum": ["opcion1", "opcion2"]},
                    "param2": {
                        "type": "string",
                        "maxLength": 6,
                        "minLength": 6,
                        "pattern": "[0-9]",
                    },
                    "param3": {
                        "type": "string",
                        "maxLength": 6,
                        "minLength": 6,
                        "pattern": "[0-9]",
                    },
                },
                "required": ["param1", "param2", "param3"],
                "additionalProperties": False,
            }

            if type(j_input).__name__ != "dict":
                return False

            validate(instance=j_input, schema=schema)

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
