# logger_util.py
import logging
from colorama import init, Fore

# Initialize colorama to work on Windows OS
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_message = super().format(record)
        return log_message

class ColoredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Set the default logging level

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Set the console handler to the lowest level

        formatter = ColoredFormatter()
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    def log(self, level, message, color=None):
        if color:
            log_message = f"{color}{message}"
        else:
            log_message = message

        getattr(self.logger, level.lower())(log_message)

    def debug(self, message, color=None):
        self.log('DEBUG', message, color)

    def info(self, message, color=None):
        self.log('INFO', message, color)

    def warning(self, message, color=None):
        self.log('WARNING', message, color)

    def error(self, message, color=None):
        self.log('ERROR', message, color)

    def critical(self, message, color=None):
        self.log('CRITICAL', message, color)
