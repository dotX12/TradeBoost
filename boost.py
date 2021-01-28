import time

import steampy.exceptions
from logger.logger_templates import *
from logger.logger_module import *
from steampy.client import SteamClient
from steampy.models import GameOptions, Asset
import json
from random import choice
from utils.vaildate_api import *
from utils.state import *

state = State()


class TradeBoost:
    GAME = GameOptions.STEAM
    translate = Locale('RU')

    def __init__(self, cfg_account, recipient_id):

        self.recipient_id = recipient_id
        self.cfg_account = json.load(open(cfg_account))
        self.partner_id = int(self.recipient_id) - 76561197960265728
        self.adapter = CustomAdapter(logger, {'account': self.cfg_account["login"]})
        try:
            self.account = SteamClient(self.cfg_account['API'])
            self.account.login(self.cfg_account['login'], self.cfg_account['password'], cfg_account)
            self.adapter.info(self.translate.word('good_auth'))
            self.decline_all_trades()
        except steampy.exceptions.InvalidCredentials as e:
            self.adapter.warning(self.translate.word('bad_auth').format(e))

    def decline_all_trades(self):
        params = {'key': self.cfg_account['API'],
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
        self.adapter.info(self.translate.word('trade_decline').format(count_decline))

    def get_item(self):
        try:
            items = self.account.get_my_inventory(game=self.GAME, count=15)
            item_id = choice(list(items.keys()))
            about_item = items[item_id]

            if item_id and state.not_in(item_id and about_item['tradable'] == 1):
                self.adapter.info(self.translate.word('item_received').format(item_id, about_item["name"]))
                state.add(item_id)
                return item_id
            else:
                return ''
        except:
            pass

    def send_trades(self):
        item_id = ''
        while item_id in ['', None]:
            item_id = self.get_item()

        asset_one = Asset(item_id, self.GAME)

        trade = self.account.make_offer([asset_one], [], self.recipient_id)
        if validate_api_response(trade) is True:
            self.adapter.info(self.translate.word('sent_trade').format(trade["tradeofferid"]))
            return trade['tradeofferid']
        else:
            self.adapter.warning(self.translate.word('bad_send').format(list(trade.values())[0]))
            self.decline_all_trades()
            resp_summary = self.account.get_trade_offers_summary()['response']
            if resp_summary['pending_received_count'] >= 3 or resp_summary['pending_sent_count'] >= 3:
                self.adapter.warning(self.translate.word('steam_wait'))
                time.sleep(60)

    def accept_trade(self, trade_id):
        trade_info = self.account.get_trade_offer(trade_id)
        if 'offer' in trade_info['response']:
            if int(trade_info['response']['offer']['accountid_other']) == self.partner_id:
                resp = self.account.accept_trade_offer(trade_id)
                if validate_api_response(resp) is True:
                    self.adapter.info(self.translate.word('accepted_trade').format(trade_id))
                    item = trade_info['response']['offer']['items_to_receive'][0]['assetid']
                    state.remove(item)
                else:
                    self.adapter.warning(self.translate.word('bad_accept').format(trade_id, list(resp.values())[0]))
        else:
            self.adapter.warning(self.translate.word('bad_send').format(trade_info))