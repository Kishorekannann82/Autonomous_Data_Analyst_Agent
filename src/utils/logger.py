from datetime import datetime


class Logger:

    @staticmethod
    def info(message):

        print(
            f"[{datetime.now()}] INFO : {message}"
        )

    @staticmethod
    def warning(message):

        print(
            f"[{datetime.now()}] WARNING : {message}"
        )

    @staticmethod
    def error(message):

        print(
            f"[{datetime.now()}] ERROR : {message}"
        )