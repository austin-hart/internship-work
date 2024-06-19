"""Holds RedisDataStore class. Used to set and get from redis."""
import pickle
import redis
from project.datastore.data_store import DataStore


class RedisDataStore(DataStore):
    """RedisDataStore class. Used to set and get from redis."""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.redis_client = redis.Redis(self.host, self.port)

    def set_key_value_pair(self, key, value):
        """Used to set key value pair on redis."""
        pickled_odds = pickle.dumps(value)
        self.redis_client.set(key, pickled_odds)

    def get_value_by_key(self, key):
        """Used to get value from key on redis."""
        unpacked_object = pickle.loads(self.redis_client.get(key))
        return unpacked_object
