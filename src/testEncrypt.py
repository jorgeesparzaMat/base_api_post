# IMPORTA LIBRERIAS PYTHON
import json
import os

# GENERA VARIABLES DE INSTANCIA
os.environ["ambiente"] = "DE"


# IMPORTA LAMBDA HANLDER
from lambda_handler import lambda_handler


# GENERA CONTEXTO
class Context:
    invoked_function_arn = (
        "arn:aws:lambda:us-east-1:254711811335:function:api_recurso_accion"
    )
    function_name = "api_recurso_accion"


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
        "cuentaid": "0",
        "Host": "q7rv3xbapb.execute-api.us-east-1.amazonaws.com",
        "requestfecha": "1646076575",
        "requestfirma": "e52e051052d60e6d518041772edc89736f070b5edaeb062b937a2a28057f452b",
        "requestid": "1NoLIb7Ln6wF8m9aYqwGuiEY8GSB0Xp0BE5a29DU",
        "requestsecret": "2c66e43d4eef919a0662edd9e6af0da4e827d40627c03017f8cf3625fba363a4c09dadae1dec0db0efc61754b8bdf110",
        "sesiontoken": "010202007887f404868f1d6e33380506d314f9ca918551b8daa67316ef30d62042d409627501f05dfb202a75871f98bd605d6fd66700000000f03081ed06092a864886f70d010706a081df3081dc0201003081d606092a864886f70d010701301e060960864801650304012e3011040cfab50f6998a277220c8806520201108081a8bee0a6ba04f1d4dc2da28a81e394b39289f1c3308ca57abe66c9d0662ab0224a372575920af78d6002a4162716ac7e547775188fe072e07a5fe865ae114e0f9c7e722f3580a67a30a696c8c440d02c437ca22835bd3999a35a016c52e8ddf3fbbaca4f081c003ae17a593d0f2cb8e3994f4a2b5d38b12e8e113bcfaafd522fa3934bf086b272365dc06c4098e2fd905c018e29ff3baa49e56f0d300182a588c15369158d1c708450",
        "ubicacionid": "0",
        "User-Agent": "python-requests/2.26.0",
        "Via": "1.1 9211c11ef620fe2dded5b3d26152b9ea.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "kiG9CuL5D1TxKdOCc1GqZXYFjcUIXH--wmlQ1E79zbJqo41SEtr39w==",
        "X-Amzn-Trace-Id": "Root=1-621d229f-2658509368e1002c46fd7e4c",
        "X-Forwarded-For": "201.189.141.127, 64.252.175.83",
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
        "cuentaid": ["0"],
        "Host": ["q7rv3xbapb.execute-api.us-east-1.amazonaws.com"],
        "requestfecha": ["1646076575"],
        "requestfirma": [
            "e52e051052d60e6d518041772edc89736f070b5edaeb062b937a2a28057f452b"
        ],
        "requestid": ["1NoLIb7Ln6wF8m9aYqwGuiEY8GSB0Xp0BE5a29DU"],
        "requestsecret": [
            "2c66e43d4eef919a0662edd9e6af0da4e827d40627c03017f8cf3625fba363a4c09dadae1dec0db0efc61754b8bdf110"
        ],
        "sesiontoken": [
            "010202007887f404868f1d6e33380506d314f9ca918551b8daa67316ef30d62042d409627501f05dfb202a75871f98bd605d6fd66700000000f03081ed06092a864886f70d010706a081df3081dc0201003081d606092a864886f70d010701301e060960864801650304012e3011040cfab50f6998a277220c8806520201108081a8bee0a6ba04f1d4dc2da28a81e394b39289f1c3308ca57abe66c9d0662ab0224a372575920af78d6002a4162716ac7e547775188fe072e07a5fe865ae114e0f9c7e722f3580a67a30a696c8c440d02c437ca22835bd3999a35a016c52e8ddf3fbbaca4f081c003ae17a593d0f2cb8e3994f4a2b5d38b12e8e113bcfaafd522fa3934bf086b272365dc06c4098e2fd905c018e29ff3baa49e56f0d300182a588c15369158d1c708450"
        ],
        "ubicacionid": ["0"],
        "User-Agent": ["python-requests/2.26.0"],
        "Via": ["1.1 9211c11ef620fe2dded5b3d26152b9ea.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["kiG9CuL5D1TxKdOCc1GqZXYFjcUIXH--wmlQ1E79zbJqo41SEtr39w=="],
        "X-Amzn-Trace-Id": ["Root=1-621d229f-2658509368e1002c46fd7e4c"],
        "X-Forwarded-For": ["201.189.141.127, 64.252.175.83"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": "",
    "multiValueQueryStringParameters": "",
    "pathParameters": "",
    "stageVariables": "",
    "requestContext": {
        "resourceId": "dtha7s",
        "authorizer": {
            "principalId": '{"request_key": "e7e8a12ca059d2bc42401a53c420ce095d2c2742e34e1278d2d73a679b0abd12", "sesion_id": "1NoLGT57XaoP4kSsoMIaOYqO84qE0X9W3NA0IYtU"}',
            "integrationLatency": 148,
        },
        "resourcePath": "/sesion",
        "httpMethod": "POST",
        "extendedRequestId": "ORJZBGQboAMF_Vg=",
        "requestTime": "28/Feb/2022:19:29:35 +0000",
        "path": "/DE/sesion",
        "accountId": "729514427247",
        "protocol": "HTTP/1.1",
        "stage": "DE",
        "domainPrefix": "q7rv3xbapb",
        "requestTimeEpoch": 1646076575926,
        "requestid": "2130705a-5e67-4f60-b0ff-59d2661b528e",
        "identity": {
            "cognitoIdentityPoolId": "",
            "accountId": "",
            "cognitoIdentityId": "",
            "caller": "",
            "sourceIp": "201.189.141.127",
            "principalOrgId": "",
            "accessKey": "",
            "cognitoAuthenticationType": "",
            "cognitoAuthenticationProvider": "",
            "userArn": "",
            "userAgent": "python-requests/2.26.0",
            "user": "",
        },
        "domainName": "q7rv3xbapb.execute-api.us-east-1.amazonaws.com",
        "apiId": "q7rv3xbapb",
    },
    "body": '{"body_encriptado": "34ec4491af8a535811c3fe4fdb1eb640f18850c7ff85ea78b1159720ad949c6047aedb4538127797d4aca9116ede4a2887db8c227ab1b53bd690f0de85ba02e0b0cb06113c1600c009450c710f5379f8916918c4003855f262c74d2a88fee70f", "body_firma": "e8d16442e1126b8e11df202380e9033d8425ab2be7f16562b2ed8ef884961d14"}',
    "isBase64Encoded": False,
}

print(lambda_handler(event, context))
