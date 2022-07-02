import json
import socket
from libs.date_time.__init__ import current_datetime_with_tz, current_datetime

class Log:
    def __init__(self, log_type, enable_warn=True):
        self.__log_type = log_type + "--" + socket.gethostname()
        self.__enable_warn = enable_warn

    def info(self, message, extra=None, time=None):
        self.print_log(message, "INFO", extra, time)

    def error(self, message, extra=None, time=None):
        self.print_log(message, "ERROR", extra, time)

    def warn(self, message, extra=None, time=None):
        if self.__enable_warn:
            self.print_log(message, "WARNING", extra, time)

    def print_log(self, message, log_level, extra, time):
        obj_log = {
            "date": current_datetime_with_tz().isoformat(),
            "log_type": self.__log_type,
            "log_level": log_level
        }
        if time:
            obj_log["time"] = str((current_datetime() - time).total_seconds())
        obj_log["msg"] = message if isinstance(message, str) else str(message)
        if extra is not None:
            for key, value in extra.items():
                obj_log[key] = value
        print(json.dumps(obj_log))
