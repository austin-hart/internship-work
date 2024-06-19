"""Holds FeedInfo."""
import time


class FeedInfo:
    """This is a class that represents a single data feed."""

    def __init__(self, price_fetcher: object, cadence: int):
        self.price_fetcher = price_fetcher
        self.last_run_ts = 0
        self.cadence = cadence
        self.uuid_str = ''
        self.ready_to_get = False

    def __eq__(self, other):
        if self.price_fetcher == other.price_fetcher and self.cadence == other.cadence:
            return True
        return False

    def get_value(self) -> dict:
        """Gets the value of the feed which is always a dict mapping to any type."""
        return self.price_fetcher.get_info()

    def get_last_run_ts(self) -> str:
        """Returns the time the feed last ran"""
        return self.last_run_ts

    def set_cadence(self, cadence: int):
        """Sets the cadence. i.e How often a request is pulled."""
        self.cadence = cadence

    def set_last_run_ts(self, last_run_ts: int):
        """Sets the last run time called in operate feed."""
        self.last_run_ts = last_run_ts

    def should_run_q(self) -> bool:
        """Returns True if enough time has passed since last run"""
        if time.time() > self.last_run_ts + self.cadence:
            return True
        return False
