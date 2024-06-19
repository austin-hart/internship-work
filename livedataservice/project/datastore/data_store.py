# pylint:disable=unnecessary-pass
"""Holds DataStore abstract class."""
from abc import abstractmethod
from typing import Any


class DataStore:
    """Creates abstract methods for storing daya by key/value."""
    @abstractmethod
    def set_key_value_pair(self, key: str, value: Any):
        """Abstarct method for setting key/value pair."""
        pass

    @abstractmethod
    def get_value_by_key(self, key: Any):
        """Abstarct method for getting value from key."""
        pass
