# pylint: skip-file
from project.service.polymarket_exchange_info import PolymarketExchangeInfo
from project.service.order_info import OrderInfo
from concurrent.futures import ThreadPoolExecutor
from project.service.websocket_connection import OrderClient
import uuid
import json
import time
from threading import Thread
import logging
import requests


class OrderManagementSystem:
    def __init__(self):
        self.previous_orders = Thread(target=self.get_prev_orders)
        self.previous_orders.setDaemon(True)
        self.previous_orders.start()
        # self.websocket_thread.submit(self.websocket_connection)
        json_file = open("project/service/exchanges.json", "r")
        json_exchanges = json.load(json_file)
        json_file.close()
        self.registered_orders = {}
        self.available_exchanges = json_exchanges["SupportedExchanges"]
        self.exchange_inits = {"Polymarket": PolymarketExchangeInfo()}

    def get_prev_orders(self):
        """Sleeps 5 seconds and pulls trade history for our 
        private key. 
        """
        while True:
            time.sleep(5)
            self.ws = OrderClient()
            self.ws.main()

    def get_supported_exchanges(self):
        return self.available_exchanges

    def get_supported_market_for_exchange(self, exchange):
        if exchange == "Polymarket":
            api_response = requests.get("https://clob.polymarket.com/markets")
            json_obj = json.loads(api_response.text)
            json_str = json.dumps(json_obj)
            return json_str
        return

    def register_order(self, exchange, market, side, price, size, kind):
        order = OrderInfo(exchange, market, side, price, size, kind)
        order.exchange = self.exchange_inits[exchange]
        uuid_form = uuid.uuid4()
        uuid_str = str(uuid_form)
        self.registered_orders[uuid_str] = order
        return uuid_str

    def place_order(self, order_id):
        try:
            order = self.registered_orders[order_id]
            confirmation = order.exchange.place_order(order)
            return confirmation
        except KeyError:
            logging.error("Order does not exist. Invalid order ID.")

    def cancel_order(self, order_id):
        try:
            order = self.registered_orders[order_id]
            exchange = order.exchange
            confirmation = exchange.cancel_order(order)
            return confirmation
        except KeyError:
            logging.error("Order does not exist. Invalid order ID.")

    def get_order_status(self, order_id):
        try:
            order = self.registered_orders[order_id]
            exchange = order.exchange
            confirmation = exchange.get_order_status(order)
            return confirmation
        except KeyError:
            logging.error("Order does not exist. Invalid order ID.")

    def get_order(self, order_id):
        return self.registered_orders[order_id]

    def get_open_orders_poly(self):
        exchange = self.exchange_inits["Polymarket"]
        return exchange.get_open_orders()

    def derive_api_key_poly(self):
        exchange = self.exchange_inits["Polymarket"]
        return exchange.derivive_api_key()
