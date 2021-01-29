from tradeboost.logger.logger_module import *


def send_trade(account):
    try:
        item = account.send_trades()
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
