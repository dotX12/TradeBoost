class Locale:
    lang = {'good_auth':
                ['Успешная авторизация в аккаунте',
                 'Successful account authorization'],
            'bad_auth':
                ['не смогли зайти в аккаунт. Причина - {}',
                 'could not log into your account. Reason - {}'],
            'bad_send':
                ['Ошибка: {}',
                 'Error: {}'],
            'trade_decline':
                ['Трейдов отменено: {}',
                 'Trades canceled: {}'],
            'item_received':
                ['Получен ID предмета: {}. Название предмета: {}',
                 'Item ID received: {}. Item name: {} '],
            'sent_trade':
                ['Отправлен трейд, его ID: {}',
                 'A trade was sent, its ID: {}'],
            'steam_wait':
                ['Сплю минуту из-за лагов Steam',
                 'I sleep for a minute due to Steam lags'],
            'accepted_trade':
                ['Trade ID: {} был принят',
                 'Trade ID: {} was accepted'],
            'bad_accept':
                ['Trade ID: {} не был принят по причине: {}',
                 "Trade ID: {} was not accepted due to: {}"],
            'added_accounts_to_memory':
                ['Добавлены аккаунты {} в память (файл counter.json), в ней можно посмотреть количество обменов.',
                 'Added accounts {} in memory (counter.json file), in it you can see the number of exchanges.'],
            'already_in_memory':
                ['Аккаунты уже были ранее добавлены в память.',
                 'Accounts have already been previously added to memory.']
            }

    def __init__(self, language):
        if language == 'RU':
            self.language = 0
        elif language == 'EN':
            self.language = 1

    def word(self, word):
        return self.lang[word][self.language]
