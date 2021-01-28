from boost import state
from utils.send_and_accept import send_trade, accept_trade


def run_program(account1, account2):

    while True:
        out = send_trade(account1)
        accept_trade(account2, out)

        out2 = send_trade(account2)
        accept_trade(account1, out2)
        print(f'Трейдов отправлено: {state.sent}')
