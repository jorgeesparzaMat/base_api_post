import hashlib
import uuid
from datetime import datetime
from random import randint

from generales.fecha import Fecha


class Token:
    @staticmethod
    def genera_token():

        token_30 = ""
        token_10 = ""

        ####################################################
        # TOKEN30
        ####################################################

        # Fecha
        now = Fecha.now_epoch_utc()
        token_30 = token_30 + Token.int2base(now, 62)

        # uuid
        uuid_4 = str(uuid.uuid4()).replace("-", "")
        uuid_4_int = int(uuid_4, 16)
        uuid_1 = str(uuid.uuid1(clock_seq=Fecha.now_epoch_utc_microsegundos())).replace(
            "-", ""
        )
        uuid_1_int = int(uuid_1, 16)
        uuid_f_int = uuid_4_int + uuid_1_int
        token_30 = token_30 + Token.int2base(uuid_f_int, 62)

        # formato token 30
        if len(token_30) > 29:
            token_30 = token_30[:29]
        else:
            token_30 = token_30.ljust(29, "0")

        token_30 = token_30[:29] + "X"

        ####################################################
        # TOKEN10
        ####################################################

        uuid_4_2 = hashlib.sha1((str(uuid.uuid4())).encode()).hexdigest()
        uuid_4_2_int = int(uuid_4_2, 16)
        token_10 = Token.int2base(uuid_4_2_int, 62)

        # formato token 10
        if len(token_10) > 10:
            token_10 = token_10[:10]
        else:
            token_10 = token_10.ljust(10, "0")

        ####################################################
        # TOKEN
        ####################################################
        token = token_30 + token_10

        return token

    @staticmethod
    def int2base(x, base):
        digs = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = []
        while x:
            digits.append(digs[int(x % base)])
            x = int(x / base)

        digits.reverse()

        return "".join(digits)
