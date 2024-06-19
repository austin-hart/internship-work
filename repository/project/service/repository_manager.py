# pylint: skip-file

from abc import abstractmethod


class RepositoryManager():
    """Will use this class to manage the repsoitory, add trades and get trades from database."""
    @abstractmethod
    def get_trade(self, start_date, end_date, market, side, offset):
        """Use trade fetcher object to get trade info and pull the data from database that matches info.
        parameters:   (trade_fetcher): trade fetcher object which has getter methods for given parametrs from grpc and to get info from database."""

        pass

    @abstractmethod
    def post_trade(self, json_data):
        """Uses json_data to post a trade to the database.
        parameters:     (json_data): json data that holds information about a single trade thats been placed."""
        pass
