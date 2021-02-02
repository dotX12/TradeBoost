from tradeboost.utils.send_and_accept import send_trade, accept_trade
from tradeboost.utils.accounts_memory import MemoryAccount


def run_program(account1, account2):

    mem = MemoryAccount(account1.login, account2.login)

    while True:
        out = send_trade(account1)
        accept_trade(account2, out)

        out2 = send_trade(account2)
        accept_trade(account1, out2)

        mem.add_trade()
