# pylint: skip-file
from project.service.exchange_info import ExchangeInfo
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import LimitOrderArgs, ApiCreds, MarketOrderArgs
import os
import dotenv
from eth_keys import keys
import codecs
from eth_account import Account
from hexbytes import HexBytes

dotenv.load_dotenv()


class PolymarketExchangeInfo(ExchangeInfo):
    def __init__(self):
        pk = os.getenv("PK")
        chain_id = 80001
        host = "https://clob-staging.polymarket.com"
        creds = ApiCreds(os.getenv("API_KEY"), os.getenv(
            "SECRET"), os.getenv("PASSPHRASE"))
        self.client = ClobClient(
            host=host, key=pk, chain_id=chain_id, creds=creds)
        # print(self.client.create_api_key())

    def place_order(self, order: object):
        if order.kind == "limit":

            order_args = LimitOrderArgs(
                price=order.price,
                size=order.size,
                side=order.side,
                token_id=order.market
            )

            limit_order = self.client.create_limit_order(order_args)
            response = self.client.post_order(limit_order)
            order.exchange_order_id = response['orderID']
            return response
        order_args = MarketOrderArgs(
            worst_price=order.price,
            size=order.size,
            side=order.side,
            token_id=order.market
        )
        market_order = self.client.create_market_order(order_args)
        response = self.client.post_order(market_order)
        order.exchange_order_id = response['orderID']
        return response

    def cancel_order(self, order):
        order_id = order.exchange_order_id
        response = self.client.cancel(order_id)
        return response

    def get_order_status(self, order):
        order_id = order.exchange_order_id
        response = self.client.get_order(order_id)
        return response

    def get_open_orders(self):
        return self.client.get_open_orders()

    def derivive_api_key(self):
        return self.client.derive_api_key()
