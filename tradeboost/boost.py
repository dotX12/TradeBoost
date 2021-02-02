import steampy.exceptions
from tradeboost.logger.logger_module import *
from steampy.client import SteamClient
from steampy.models import GameOptions, Asset
import json
from random import choice
from language import translate
from tradeboost.utils.vaildate_api import *
from tradeboost.utils.state import *

state = State()


class TradeBoost:
    GAME = GameOptions.STEAM

    def __init__(self, cfg_account: str, recipient_id: str) -> None:

        self.cfg_account = json.load(open(cfg_account))
        self.login = self.cfg_account["login"]
        self.api_token = self.cfg_account['API']
        self.password = self.cfg_account['password']
        self.recipient_id = recipient_id
        self.partner_id = int(self.recipient_id) - 76561197960265728
        self.adapter = CustomAdapter(logger, {'account': self.login})

        try:
            self.account = SteamClient(self.api_token)
            self.account.login(self.login, self.password, cfg_account)
            self.adapter.info(translate.word('good_auth'))
            self.decline_all_trades()

        except steampy.exceptions.InvalidCredentials as e:
            self.adapter.warning(translate.word('bad_auth').format(e))

    def decline_all_trades(self):

        params = {'key': self.api_token,
                  'get_sent_offers': 1,
                  'get_received_offers': 0,
                  'get_descriptions': 0,
                  'language': 'english',
                  'active_only': 1,
                  'historical_only': 0,
                  'time_historical_cutoff': ''}
        response = (self.account.api_call('GET', 'IEconService', 'GetTradeOffers', 'v1', params).json()['response'])
        count_decline = 0
        if 'trade_offers_sent' in response:
            for offer in response['trade_offers_sent'][:5]:
                if offer['accountid_other'] == self.partner_id:
                    self.account.cancel_trade_offer(offer['tradeofferid'])
                    count_decline += 1
        self.adapter.info(translate.word('trade_decline').format(count_decline))

    def get_item(self) -> str:

        try:
            items = self.account.get_my_inventory(game=self.GAME, count=15)
            item_id = choice(list(items.keys()))
            about_item = items[item_id]
            if item_id and state.not_in(item_id) and about_item['tradable'] == 1:
                self.adapter.info(translate.word('item_received').format(item_id, about_item["name"]))
                state.add(item_id)
                return item_id
            else:
                return ''
        except Exception as e:
            self.adapter.warning(translate.word('bad_send').format(e))
            return ''

    def send_trades(self) -> str:
        item_id = ''
        while item_id in ['', None]:
            item_id = self.get_item()

        asset_one = Asset(item_id, self.GAME)

        trade = self.account.make_offer([asset_one], [], self.recipient_id)
        if validate_api_response(trade):
            self.adapter.info(translate.word('sent_trade').format(trade["tradeofferid"]))
            return trade['tradeofferid']
        else:
            self.adapter.warning(translate.word('bad_send').format(list(trade.values())[0]))
            self.decline_all_trades()

    def accept_trade(self, trade_id: str) -> None:
        trade_info = self.account.get_trade_offer(trade_id)
        if 'offer' in trade_info['response']:
            if int(trade_info['response']['offer']['accountid_other']) == self.partner_id:
                resp = self.account.accept_trade_offer(trade_id)
                if validate_api_response(resp):
                    self.adapter.info(translate.word('accepted_trade').format(trade_id))
                    item = trade_info['response']['offer']['items_to_receive'][0]['assetid']
                    state.remove(item)
                else:
                    self.adapter.warning(translate.word('bad_accept').format(trade_id, list(resp.values())[0]))
        else:
            self.adapter.warning(translate.word('bad_send').format(trade_info))
