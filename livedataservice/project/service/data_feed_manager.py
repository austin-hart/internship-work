# pylint:disable=invalid-name, unused-variable, too-few-public-methods, attribute-defined-outside-init, line-too-long, bare-except
"""
This program pulls odds data from the odds API every one second for the sport
of your choosing. It will pull from mulitple bookmakers and average the probabilities. It then
pushes the data to redis so it can be easily retrieved.
"""


import time
import uuid
from concurrent.futures import ThreadPoolExecutor
import logging
from project.service.feed_info import FeedInfo


class DataFeedManager:
    """Manages all the data feeds and has methods to operate on them."""

    def __init__(self, datastore):
        self.datastore = datastore
        self.feeds = {}
        self.registers = {}
        self.started = False
        self.stopped = False
        self.executor = ThreadPoolExecutor(5)

    def __del__(self):
        try:
            self.executor.shutdown()
        except:
            pass

    def register_feed(self, price_fetcher: object, cadence: int):
        """
        Registers a feed(s) by initalizing it as a FeedInfo object.
        and assigns it a uuid.
        """
        feed = FeedInfo(price_fetcher, cadence)
        if feed not in self.feeds.values():
            uuid_form = uuid.uuid4()
            uuid_str = str(uuid_form)
            self.feeds[uuid_str] = feed
            self.registers[uuid_str] = 1
            feed.uuid_str = uuid_str
            return uuid_str
        logging.info('FEED ALREADY EXISTS. RETURNING EXISTING UUID')
        for uuid_str, o_feed in self.feeds.items():
            if feed == o_feed:
                self.registers[uuid_str] += 1
                return uuid_str
        return ''

    def start(self):
        """Starts the thread pool by sumbiting the run method to it."""
        self.executor.submit(self.run())

    def stop(self):
        """Stops the thread pool."""
        logging.info('SHUTTING DOWN THREAD POOL.')
        self.stopped = True
        self.started = False
        self.executor.shutdown()

    def run(self):
        """Main while loop that uses the thread pool to operate on the feeds."""
        logging.info('THREAD POOL EXECUTED.')
        while not self.stopped:
            self.executor.map(self.operate_feed, self.feeds.keys())
            time.sleep(1)

    def operate_feed(self, uuid_str: str):
        """Sets the uuid to the feed value on redis using datastore."""
        feed = self.feeds[uuid_str]
        if feed.should_run_q():
            value = feed.get_value()
            value_dict = {'value': value}
            self.datastore.set_key_value_pair(key=uuid_str, value=value_dict)
            logging.info('SET FEED %s VALUE TO REDIS.', uuid_str)
            if feed.ready_to_get is False:
                feed.ready_to_get = True
        feed.set_last_run_ts(time.time())

    def get_value_by_uuid(self, uuid_str: str):
        """Gets value by uuid from redis using datastore."""
        feed = self.feeds[uuid_str]
        if feed.ready_to_get:
            logging.info('GET FEED %s FROM REDIS.', uuid_str)
            value = self.datastore.get_value_by_key(key=uuid_str)
            return value
        return {}

    def delete_feed(self, uuid_str: str):
        """Deletes a feed and unregisters it."""
        self.registers[uuid_str] -= 1
        if self.registers[uuid_str] == 0:
            logging.info('DELETED FEED %s.', uuid_str)
            del self.feeds[uuid_str]


# ODDS API EXAMPLE
# strategy feeds this data to service in proto file?: 'baseball_mlb', 'h2h', '2c370783f34c42373d4a8a98b8218eb6' which is a specfifc baseball match
# OddsApiPriceFetcher gets a feed, and DataFeedManager registers the feed and returns an ID for a feed back to the strategy
# strategy can then call DataFeedManager.get_value_by_id(ID) which returns FEED
# strategy can then call FEED.get_value() to get specfifc price data in a list
