import logging

_log_format = (f"%(asctime)s - [%(levelname)s] - %(name)s - "
                   f"(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")


class ContextFilter(logging.Filter):

    def __init__(self, account):
        super().__init__(account)
        self.account = account

    def filter(self, record):
        record.account = self.account
        return True


def get_file_handler():
    file_handler = logging.FileHandler("../log.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format, datefmt='%d-%m-y %H:%M:%S'))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format, datefmt='%d-%m-%Y %H:%M:%S'))
    return stream_handler


class CustomAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        return '%s : %s' % (self.extra['account'], msg), kwargs


logger = logging.getLogger('BOOST')
logger.setLevel(logging.INFO)
logger.addHandler(get_file_handler())
logger.addHandler(get_stream_handler())
