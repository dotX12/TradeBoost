from boost import state
from logger.logger_module import *


def send_trade(account):
    try:
        item = account.send_trades()
        state.add_sent()
        return item
    except Exception as e:
        logger.warning(e)
        pass


def accept_trade(account, item):
    try:
        account.accept_trade(item)
    except Exception as e:
        logger.warning(e)
        pass