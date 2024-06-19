import unittest
from project.service.data_feed_manager import DataFeedManager
from project.service.odds_api_price_fetcher import OddsApiPriceFetcher
from project.service.utilities import Utilities
from project.service.feed_info import FeedInfo
from unittest import mock


def get_successful_mock_response_json():
    f = open('./tests/response.txt', 'r')
    text = f.read()
    f.close()
    return text


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.text = json_data
            self.status_code = status_code

        def json(self):
            return self.text

    if args[0] == 'https://api.the-odds-api.com/v4/sports/baseball_mlb/odds':
        return MockResponse(get_successful_mock_response_json(), 200)
    elif args[0] == 'https://api.the-odds-api.com/v4/sports/baseball/odds':
        return MockResponse(None, 404)


def mocked_time_time():
    return 1653412460.673398


def mocked_uuid_uuid4():
    class MockedUuid:
        def __str__(self):
            return 'b10550a7-1b62-4166-91b8-18e173f87c0d'
    return MockedUuid()


class MockRedis:
    def __init__(self):
        self.cache = dict()

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return None

    def set(self, key, value, *args, **kwargs):
        self.cache[key] = value


class MockDataStore:
    def __init__(self):
        self.redis_client = MockRedis()

    def set_key_value_pair(self, key, value):
        self.redis_client.set(key, value)

    def get_value_by_key(self, key):
        return self.redis_client.get(key)


class MockExecutor():
    def __init__(self):
        self.submit_counts = 0
        self.map_counts = 0

    def submit(self):
        self.submit_counts += 1

    def map(self, method, iter):
        self.map_counts += 1


class IfRunning:
    def __init__(self):
        self.running = False

    def loop(self):
        self.running = True


class Tests(unittest.TestCase):
    # tests Utilities class methods
    def test_american_to_probability(self):
        self.assertEqual(Utilities.american_to_probability(-115), 53.49)
        self.assertEqual(Utilities.american_to_probability(-300), 75)
        self.assertEqual(Utilities.american_to_probability(-177), 63.9)
        self.assertEqual(Utilities.american_to_probability(100), 50)
        self.assertEqual(Utilities.american_to_probability(144), 40.98)
        self.assertEqual(Utilities.american_to_probability(183), 35.34)
        self.assertEqual(Utilities.american_to_probability(300), 25)

    # tests OddsApiPriceFetcher class methods
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_info(self, mock_get):
        odds_api_price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        odds_api_price_fetcher_2 = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7fcd8047f07890e929841ac9dc004563')
        odds_api_price_fetcher_3 = OddsApiPriceFetcher(
            'baseball', 'h2h', '7fcd8047f07890e929841ac9dc004563')
        self.assertEqual(odds_api_price_fetcher.get_info(), [
                         ('7240dac1576130103d0c7e9d3542c773', [34.49, 69.23])])
        self.assertEqual(odds_api_price_fetcher_2.get_info(), [
                         ('7fcd8047f07890e929841ac9dc004563', [42.33, 61.04])])
        self.assertEqual(odds_api_price_fetcher_3.get_info(
        ), 'Failed to get odds: status_code 404. Status Code 400-499 = Client Error.')

    def test_get_sport(self):
        odds_api_price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        self.assertEqual(odds_api_price_fetcher.get_sport(), 'baseball_mlb')

    def test_get_market(self):
        odds_api_price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        self.assertEqual(odds_api_price_fetcher.get_market(), 'h2h')

    def test_eq_price_fetcher(self):
        odds_api_price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        odds_api_price_fetcher_2 = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        odds_api_price_fetcher_3 = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7fcd8047f07890e929841ac9dc004563')
        self.assertEqual(odds_api_price_fetcher ==
                         odds_api_price_fetcher_2, True)
        self.assertEqual(odds_api_price_fetcher ==
                         odds_api_price_fetcher_3, False)

    # tests feed info class methods
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_value(self, mock_get):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info = FeedInfo(price_fetcher, 1)
        price_fetcher_2 = OddsApiPriceFetcher(
            'baseball', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info_2 = FeedInfo(price_fetcher_2, 1)
        self.assertEqual(feed_info.get_value(), [
                         ('7240dac1576130103d0c7e9d3542c773', [34.49, 69.23])])
        self.assertEqual(feed_info_2.get_value(
        ), 'Failed to get odds: status_code 404. Status Code 400-499 = Client Error.')

    def test_eq_feed_info(self):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info = FeedInfo(price_fetcher, 1)
        price_fetcher_2 = OddsApiPriceFetcher(
            'baseball', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info_2 = FeedInfo(price_fetcher_2, 1)
        price_fetcher_3 = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info_3 = FeedInfo(price_fetcher_3, 1)
        self.assertEqual(feed_info == feed_info_2, False)
        self.assertEqual(feed_info == feed_info_3, True)

    def test_set_cadence(self):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info = FeedInfo(price_fetcher, 1)
        feed_info.set_cadence(2)
        self.assertEqual(feed_info.cadence, 2)

    def test_set_last_run_ts(self):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info = FeedInfo(price_fetcher, 1)
        feed_info.set_last_run_ts(2)
        self.assertEqual(feed_info.last_run_ts, 2)

    @mock.patch('time.time', side_effect=mocked_time_time)
    def test_should_run_q(self, mock_get):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        feed_info = FeedInfo(price_fetcher, 1)
        feed_info.set_last_run_ts(1653412457.673398)
        self.assertEqual(feed_info.should_run_q(), True)
        feed_info.set_last_run_ts(1653412460.673398)
        self.assertEqual(feed_info.should_run_q(), False)

    # tests DataFeedManager class methods
    @mock.patch('uuid.uuid4', side_effect=mocked_uuid_uuid4)
    def test_register_feed(self, mock_get):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        data_store = MockDataStore()
        data_feed_manager = DataFeedManager(data_store)
        self.assertEqual(data_feed_manager.register_feed(
            price_fetcher, cadence=1), 'b10550a7-1b62-4166-91b8-18e173f87c0d')
        # adding the feed to test if it is feed.values()
        data_feed_manager.register_feed(price_fetcher, cadence=1)
        self.assertEqual(data_feed_manager.register_feed(
            price_fetcher, cadence=1), 'b10550a7-1b62-4166-91b8-18e173f87c0d')

    @mock.patch('time.time', side_effect=mocked_time_time)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_operate_feed(self, mock_get, mock_get_2):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        data_store = MockDataStore()
        data_feed_manager = DataFeedManager(data_store)
        id = data_feed_manager.register_feed(price_fetcher, cadence=1)
        feed = data_feed_manager.feeds[id]
        data_feed_manager.operate_feed(id)
        self.assertEqual(feed.ready_to_get, True)
        self.assertEqual(data_feed_manager.datastore.get_value_by_key(
            id), {'value': [('7240dac1576130103d0c7e9d3542c773', [34.49, 69.23])]})
        self.assertEqual(feed.last_run_ts, 1653412460.673398)

    @mock.patch('uuid.uuid4', side_effect=mocked_uuid_uuid4)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_value_by_uuid(self, mock_get, mock_get_2):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        data_store = MockDataStore()
        data_feed_manager = DataFeedManager(data_store)
        id = data_feed_manager.register_feed(price_fetcher, cadence=1)
        feed = data_feed_manager.feeds[id]
        data_feed_manager.operate_feed(id)
        self.assertEqual(data_feed_manager.get_value_by_uuid(
            id), {'value': [('7240dac1576130103d0c7e9d3542c773', [34.49, 69.23])]})

    @mock.patch('uuid.uuid4', side_effect=mocked_uuid_uuid4)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_delete_feed(self, mock_get, mock_get_2):
        price_fetcher = OddsApiPriceFetcher(
            'baseball_mlb', 'h2h', '7240dac1576130103d0c7e9d3542c773')
        data_store = MockDataStore()
        data_feed_manager = DataFeedManager(data_store)
        id = data_feed_manager.register_feed(price_fetcher, cadence=1)
        self.assertEqual(data_feed_manager.registers[id], 1)
        data_feed_manager.delete_feed(id)
        self.assertEqual(data_feed_manager.registers[id], 0)
        self.assertEqual(id in data_feed_manager.feeds, False)

    @mock.patch("time.sleep", side_effect=InterruptedError)
    def test_start_and_run(self, mocked_sleep):
        data_store = MockDataStore()
        data_feed_manager = DataFeedManager(data_store)
        data_feed_manager.executor = MockExecutor()
        # patched time.sleep to interupt the infitinte loop
        # asserts that it is interuppted which means start called run and run
        # called operate feed
        self.assertRaises(InterruptedError, data_feed_manager.start)


if __name__ == '__main__':
    unittest.main()
