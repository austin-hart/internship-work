import unittest
from project.service.order_management_system import OrderManagementSystem
from project.service.polymarket_exchange_info import PolymarketExchangeInfo
from project.service.order_info import OrderInfo
from project.grpcdocs import oms_pb2
from project.grpcdocs.server import OrderManagementSystemServicer
import json
# from project.service.datastore
from unittest import mock


def mocked_uuid():
    return "abcd-1234-wxyz"


def mocked_exchange_place_order(uuid):
    return "OK"


def mocked_exchange_cancel_order(uuid):
    return "OK"


def mocked_exchange_get_order_status(uuid):
    return "OK"


def get_successful_mock_response_json():
    data = '[{"tokenID":"58410023360445133337002742789209293559332988923893081558084399803488340569229","minimumOrderSize":"15","minimumTickSize":"0.01","conditionId":"0x98c01e1f5053e57fcb59add64b9c0f74ac784609b80ab1a8754e934878468310"}]'
    return data


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.status_code = status_code

        def json(self):
            return self.text

    if args[0] == "https://clob.polymarket.com/markets":
        return MockResponse(get_successful_mock_response_json(), 200)


class TestOMS(unittest.TestCase):
    @mock.patch('uuid.uuid4', side_effect=mocked_uuid)
    @mock.patch('project.service.polymarket_exchange_info.PolymarketExchangeInfo.place_order', side_effect=mocked_exchange_place_order)
    def test_register_and_place_order(self, mocked_requests_get, mocked_exchange_place_order):
        oms = OrderManagementSystem()
        uuid = oms.register_order(
            "Polymarket", "dodgers-diamondbacks-abc123", "buy", .38, 100, "limit")
        confirmation = oms.place_order(uuid)
        self.assertEqual(confirmation, "OK")

    @mock.patch('uuid.uuid4', side_effect=mocked_uuid)
    @mock.patch('project.service.polymarket_exchange_info.PolymarketExchangeInfo.cancel_order', side_effect=mocked_exchange_place_order)
    def test_cancel_order(self, mocked_requests_get, mocked_exchange_cancel_order):
        oms = OrderManagementSystem()
        uuid = oms.register_order(
            "Polymarket", "dodgers-diamondbacks-abc123", "buy", .38, 100, "limit")
        confirmation = oms.cancel_order(uuid)
        self.assertEqual(confirmation, "OK")

    @mock.patch('uuid.uuid4', side_effect=mocked_uuid)
    @mock.patch('project.service.polymarket_exchange_info.PolymarketExchangeInfo.get_order_status', side_effect=mocked_exchange_get_order_status)
    def test_get_order_status(self, mocked_requests_get, mocked_exchange_get_order_status):
        oms = OrderManagementSystem()
        uuid = oms.register_order(
            "Polymarket", "dodgers-diamondbacks-abc123", "buy", .38, 100, "limit")
        confirmation = oms.get_order_status(uuid)
        self.assertEqual(confirmation, "OK")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_market_for_exchange(self, mocked_requests_get):
        oms = OrderManagementSystem()
        confirmation = oms.get_supported_market_for_exchange("Polymarket")
        self.assertEqual(
            confirmation, '[{"tokenID": "58410023360445133337002742789209293559332988923893081558084399803488340569229", "minimumOrderSize": "15", "minimumTickSize": "0.01", "conditionId": "0x98c01e1f5053e57fcb59add64b9c0f74ac784609b80ab1a8754e934878468310"}]')
