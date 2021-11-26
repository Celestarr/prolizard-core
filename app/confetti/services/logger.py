import json
from enum import Enum
from urllib.parse import urljoin

import requests
from django.conf import settings


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5


class Logger:
    def __init__(self) -> None:
        self.server_url = settings.FLUENTD_SERVER_URL

    def _log(self, log_level: LogLevel, message_obj: dict):
        try:
            url = urljoin(self.server_url, "confetti.access")
            res = requests.post(
                url,
                params={
                    "json": json.dumps(
                        {
                            **message_obj,
                            "level": log_level.name,
                        }
                    )
                },
                timeout=3,
            )
            res.raise_for_status()
        except Exception as e:
            print(str(e))

    def debug(self, message_obj: dict):
        self._log(LogLevel.DEBUG, message_obj)

    def info(self, message_obj: dict):
        self._log(LogLevel.INFO, message_obj)

    def error(self, message_obj: dict):
        self._log(LogLevel.ERROR, message_obj)

    def fatal(self, message_obj: dict):
        self._log(LogLevel.FATAL, message_obj)

    def warning(self, message_obj: dict):
        self._log(LogLevel.WARNING, message_obj)


logger = Logger()

__all__ = ["logger"]
