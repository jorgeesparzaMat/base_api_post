import decimal
import json
import os
import sys

import boto3
from boto3.dynamodb.conditions import Attr, Key
from botocore.config import Config


class DynamoDb:
    @staticmethod
    def resource_custom():
        my_config = Config(region_name="us-east-1", connect_timeout=3, read_timeout=3)
        var = boto3.resource("dynamodb", config=my_config)
        return var

    @staticmethod
    def client_custom():
        my_config = Config(region_name="us-east-1", connect_timeout=3, read_timeout=3)
        var = boto3.client("dynamodb", config=my_config)
        return var

    ################################################
    ################################################
    ################################################
    # FUNCIONES ESPECIFICAS PARA LAMBDA
    ################################################
    ################################################
    ################################################

    ################################################
    # FUNCIONES UTILITARIAS LAMBDA
    ################################################
    @staticmethod
    def dict_to_item(raw):
        boto3.resource("dynamodb")
        serializer = boto3.dynamodb.types.TypeSerializer()
        diccionario_aux_raw = json.loads(
            json.dumps({k: v for k, v in raw.items()}), parse_float=decimal.Decimal
        )
        diccionario = {
            k: serializer.serialize(v) for k, v in diccionario_aux_raw.items()
        }
        string_dict = json.dumps(diccionario, indent=4)
        return json.loads(string_dict, parse_float=decimal.Decimal)

    @staticmethod
    def item_to_dict(raw):
        boto3.resource("dynamodb")
        deserializer = boto3.dynamodb.types.TypeDeserializer()
        return json.loads(
            json.dumps(
                {k: deserializer.deserialize(v) for k, v in raw.items()},
                indent=4,
                cls=DecimalEncoder,
            )
        )


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
