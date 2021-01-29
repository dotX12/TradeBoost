from logger.logger_templates import Locale
from boost import TradeBoost
from utils.run import run_program
from tokens import *

acc_1 = TradeBoost(account_1[0], account_1[1])
acc_2 = TradeBoost(account_2[0], account_2[1])


run_program(acc_1, acc_2)
