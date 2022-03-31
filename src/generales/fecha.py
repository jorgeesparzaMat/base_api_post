import calendar
import json
import os
import sys
import time
from datetime import datetime, timedelta


class Fecha:
    @staticmethod
    def now_epoch_utc():
        fecha_now = datetime.utcnow()
        fecha_epoch = calendar.timegm(fecha_now.timetuple())
        return int(fecha_epoch)

    @staticmethod
    def now_epoch_local():
        fecha_now = datetime.now()
        fecha_epoch = time.mktime(fecha_now.timetuple())
        return int(fecha_epoch)

    @staticmethod
    def now_epoch_utc_microsegundos():
        fecha_now = datetime.utcnow()
        fecha_epoch = calendar.timegm(fecha_now.timetuple())
        fecha_epoch = int(fecha_epoch * 1000000 + fecha_now.microsecond)
        return int(fecha_epoch)

    @staticmethod
    def now_epoch_utc_milisegundos():
        fecha_now = datetime.utcnow()
        fecha_epoch = calendar.timegm(fecha_now.timetuple())
        fecha_epoch = int(fecha_epoch * 1000 + int(fecha_now.microsecond / 1000))
        return int(fecha_epoch)

    @staticmethod
    def now_epoch_utc_centisegundos():
        fecha_now = datetime.utcnow()
        fecha_epoch = calendar.timegm(fecha_now.timetuple())
        fecha_epoch = int(fecha_epoch * 100 + int(fecha_now.microsecond / 10000))
        return int(fecha_epoch)

    @staticmethod
    def epoch_utc_horas(horas):
        fecha_now = datetime.utcnow() + timedelta(hours=horas)
        fecha_epoch = calendar.timegm(fecha_now.timetuple())
        return int(fecha_epoch)

    @staticmethod
    def epoch_local_horas(horas):
        fecha_now = datetime.now() + timedelta(hours=horas)
        fecha_epoch = time.mktime(fecha_now.timetuple())
        return int(fecha_epoch)

    @staticmethod
    def now_yyyymmddhhmmss_utc():
        fecha_now = datetime.utcnow()
        fecha_yyyymmddhhmmss = fecha_now.strftime("%Y%m%d%H%M%S")
        return fecha_yyyymmddhhmmss

    @staticmethod
    def now_yyyymmdd_utc():
        fecha_now = datetime.utcnow()
        fecha_yyyymmdd = fecha_now.strftime("%Y%m%d")
        return fecha_yyyymmdd

    @staticmethod
    def now_yyyymmddhhmmss_local():
        fecha_now = datetime.now()
        fecha_yyyymmddhhmmss = fecha_now.strftime("%Y%m%d%H%M%S")
        return fecha_yyyymmddhhmmss
