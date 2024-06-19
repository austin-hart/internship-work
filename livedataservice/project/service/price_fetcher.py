# pylint:disable=too-few-public-methods, unnecessary-pass
"""Holds abstract class PriceFetcher"""
from abc import abstractmethod


class PriceFetcher:
    """Fetches dem prices hoe."""
    @abstractmethod
    def get_info(self):
        """Method to fetch prices"""
        pass
