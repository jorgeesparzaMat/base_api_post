# IMPORTA LIBRERIAS PYTHON
import json
import os

# GENERA VARIABLES DE INSTANCIA
os.environ["ambiente"] = "DE"

# IMPORTA LIBRERIA DE ENCRIPTACION
from generales.aes import Aes

# IMPORTA LAMBDA HANLDER
from lambda_handler import lambda_handler


################################################
# GENERA CONTEXTO
################################################
class Context:
    invoked_function_arn = (
        "arn:aws:lambda:us-east-1:254711811335:function:api_recurso_accion"
    )
    function_name = "api_recurso_accion"


################################################
# GENERA BODY ENCRIPTADO PARA TEST
################################################

# KEYS DE ENCRIPTACION
request_key = "9795b595101fe641b9cce9db85770dbef8e26a507589913a4b2deedd85ebff5d"
request_secret = "010202007862c26ab61d972434fe76f3cbd699abad12b1f202a738e5b946f569"
body_firma = "fed07012cda108393cf485bc02985f782a1fdc20c37efa0ce48f3884c499befd"


# BODY INPUT
body_json = {
    "usuario_telefono": "56968324270",
}

# ENCRIPTA BODY
respuesta_encrytp = Aes.encrypt_body(
    bytes.fromhex(request_key),
    request_secret[16:32].encode("utf-8"),
    json.dumps(body_json),
)

# GENERA BODY DE API
body = {
    "body_encriptado": respuesta_encrytp["body_encriptado"],
    "body_firma": respuesta_encrytp["body_firma"],
}


################################################
# GENERA INPUT
################################################
context = Context()

event = {
    "resource": "/sesion",
    "path": "/sesion",
    "httpMethod": "POST",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "CL",
        "cuentaid": "801275341361",
        "Host": "r6eelc0amg.execute-api.us-east-1.amazonaws.com",
        "requestfecha": "1645475734",
        "requestfirma": request_key,
        "requestid": "1Nmfpbcj3vab2S1asmCcAC4QSSyD0X1iNj89WpWc",
        "requestsecret": request_secret,
        "sesiontoken": "01020200780cf43c9cedc36c58959481d1b59bdc562d97ca1af7bf26e84a9229189146a8c201e50952c25209bf51ab3cbb9d31a07ab3000000f03081ed06092a864886f70d010706a081df3081dc0201003081d606092a864886f70d010701301e060960864801650304012e3011040c8dfc27c187ee71249d7ab8550201108081a82d1a70d99d7289dae6691e91df5ea42b617c33105ea5ef495b0010466f183df0e7e6a3470a819cb0665451bad178592b145dbbb5ef92201c8e0123c4d3ac6635661c04ada9b973420723ae34b8c59c69cf9d076477d5b6b8b37ca0e1005347453db25e90499ef0250c5fbbb7c97942fad676e112310dd1819e524d51762eb723e56a0c41e26dd7332081cb70821ea8741382e400e2b5f62238dea47a7e817dbde1cd813c8d18be02",
        "ubicacionid": "801275341361",
        "User-Agent": "python-requests/2.26.0",
        "Via": "1.1 078213358ed22cd95c76373c4ed65b5a.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "jXJ3DGr7WO3cmAXQsPlAtBEqYkEJZWOX2SZ3C-tKxx1qsntVN6x0kw==",
        "X-Amzn-Trace-Id": "Root=1-6213f7b0-1e76188823892f253a4a3929",
        "X-Forwarded-For": "186.67.195.66, 130.176.100.146",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
    },
    "multiValueHeaders": {
        "Accept": ["*/*"],
        "Accept-Encoding": ["gzip, deflate"],
        "CloudFront-Forwarded-Proto": ["https"],
        "CloudFront-Is-Desktop-Viewer": ["true"],
        "CloudFront-Is-Mobile-Viewer": ["false"],
        "CloudFront-Is-SmartTV-Viewer": ["false"],
        "CloudFront-Is-Tablet-Viewer": ["false"],
        "CloudFront-Viewer-Country": ["CL"],
        "cuentaid": ["801275341361"],
        "Host": ["r6eelc0amg.execute-api.us-east-1.amazonaws.com"],
        "requestfecha": ["1645475734"],
        "requestfirma": [request_key],
        "requestid": ["1Nmfpbcj3vab2S1asmCcAC4QSSyD0X1iNj89WpWc"],
        "requestsecret": [request_secret],
        "sesiontoken": [
            "01020200780cf43c9cedc36c58959481d1b59bdc562d97ca1af7bf26e84a9229189146a8c201e50952c25209bf51ab3cbb9d31a07ab3000000f03081ed06092a864886f70d010706a081df3081dc0201003081d606092a864886f70d010701301e060960864801650304012e3011040c8dfc27c187ee71249d7ab8550201108081a82d1a70d99d7289dae6691e91df5ea42b617c33105ea5ef495b0010466f183df0e7e6a3470a819cb0665451bad178592b145dbbb5ef92201c8e0123c4d3ac6635661c04ada9b973420723ae34b8c59c69cf9d076477d5b6b8b37ca0e1005347453db25e90499ef0250c5fbbb7c97942fad676e112310dd1819e524d51762eb723e56a0c41e26dd7332081cb70821ea8741382e400e2b5f62238dea47a7e817dbde1cd813c8d18be02"
        ],
        "ubicacionid": ["801275341361"],
        "User-Agent": ["python-requests/2.26.0"],
        "Via": ["1.1 078213358ed22cd95c76373c4ed65b5a.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["jXJ3DGr7WO3cmAXQsPlAtBEqYkEJZWOX2SZ3C-tKxx1qsntVN6x0kw=="],
        "X-Amzn-Trace-Id": ["Root=1-6213f7b0-1e76188823892f253a4a3929"],
        "X-Forwarded-For": ["186.67.195.66, 130.176.100.146"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": "",
    "multiValueQueryStringParameters": "",
    "pathParameters": "",
    "stageVariables": "",
    "requestContext": {
        "resourceId": "0duwl5",
        "authorizer": {
            "principalId": '{"usuario_data": {"usuario_telefono": "56968324270", "usuario_mail": "jorge.esparza@hfsolutions.cl", "privilegios_ubicacion": [], "privilegios_organizacion": [], "privilegios_cuenta": [], "es_raiz": "no", "usuario_id": "1NtIKrccRkZL9oAwsSuKmkIYOe6C0Xht2m3vGHyS", "usuario_nombre": "Jorge", "dependencia": {"cuenta_id": "926741150314", "cuenta_tipo": "organizacion", "organizacion_id": "926741150314"}, "usuario_apellido": "Esparza", "usuario_estado": "vigente"}, "request_key":"'
            + request_key
            + '", "sesion_id": "1NtJ4n6XBdn9SXbqCk8KOgYIG4as0XqTpZ06zI8o", "sesion_tipo": "usuario_ingreso", "cuenta_id": "926741150314", "cuenta_tipo": "organizacion", "organizacion_id": "926741150314", "ubicacion_id": "0"}',
            "integrationLatency": 1059,
        },
        "resourcePath": "/sesion",
        "httpMethod": "POST",
        "extendedRequestId": "N6OjmGPgIAMFb4g=",
        "requestTime": "21/Feb/2022:20:36:00 +0000",
        "path": "/DE/sesion",
        "accountId": "729514427247",
        "protocol": "HTTP/1.1",
        "stage": "DE",
        "domainPrefix": "r6eelc0amg",
        "requestTimeEpoch": 1645475760477,
        "requestid": "101d69f1-2fcc-40b6-8bad-1d5308a10265",
        "identity": {
            "cognitoIdentityPoolId": "",
            "accountId": "",
            "cognitoIdentityId": "",
            "caller": "",
            "sourceIp": "186.67.195.66",
            "principalOrgId": "123456789012",
            "accessKey": "",
            "cognitoAuthenticationType": "",
            "cognitoAuthenticationProvider": "",
            "userArn": "",
            "userAgent": "python-requests/2.26.0",
            "user": "",
        },
        "domainName": "r6eelc0amg.execute-api.us-east-1.amazonaws.com",
        "apiId": "r6eelc0amg",
    },
    "body": json.dumps(body),
    "isBase64Encoded": False,
}

print(lambda_handler(event, context))
