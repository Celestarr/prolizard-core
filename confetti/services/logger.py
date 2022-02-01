from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5


class Logger:
    def __init__(self) -> None:
        self.server_url = ""

    def _log(self, log_level: LogLevel, message_obj: dict):
        pass

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
