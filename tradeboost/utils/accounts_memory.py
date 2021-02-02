import json
from tradeboost.logger.logger_module import *


class MemoryAccount:
    def __init__(self, account1: str, account2: str):
        self.path = 'tradeboost/logger/counter.json'
        self.accounts = f'{account1}_{account2}'
        with open(self.path) as file:
            self.data = json.load(file)
        self.new_account()

    def new_account(self):
        if self.accounts not in self.data:
            self.data[self.accounts] = 0
            with open(self.path, 'w') as file:
                json.dump(self.data, file)
            print('Аккаунты были созданы.')
        else:
            print('Аккаунты уже созданы')

    def add_trade(self, count: int=2):
        self.data[self.accounts] += count
        with open(self.path, 'w') as file:
            json.dump(self.data, file)
