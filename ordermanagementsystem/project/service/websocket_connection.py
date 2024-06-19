# pylint: skip-file
from concurrent.futures import ThreadPoolExecutor
import time
import json
import logging
import websocket
import os
import threading
from py_clob_client.client import ClobClient, ApiCreds

logging.basicConfig(
    format="%(message)s",
    level=logging.DEBUG,
)


class OrderClient:
    def __init__(self):
        pk = os.getenv("PK")
        chain_id = 137
        host = "https://clob-staging.polymarket.com/"
        creds = ApiCreds(os.getenv("API_KEY"), os.getenv(
            "SECRET"), os.getenv("PASSPHRASE"))
        self.client = ClobClient(
            host=host, key=pk, chain_id=chain_id, creds=creds)
        # self.client.cancel_all()
        self.sync_orders_thread = ThreadPoolExecutor(1)
        self.recorded_orders = {}

    def sync_orders(self):
        self.order_history = self.client.get_order_history()
        self.order_history_list = self.order_history['history']
        print(self.order_history_list)
        return self.order_history_list

    def main(self):
        return self.sync_orders()
