#!/usr/bin/env python3
"""
Cache module
"""


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class to store data in Redis
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis and return the key

        Args:
            data (Union[str, bytes, int, float]): The data to be stored

        Returns:
            str: The key under which the data is stored in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> bytes:
        """
        Retrieve data from the Redis cache using the provided key.

        Args:
            key: The key under which the data is stored in the cache.
            fn: An optional callable to convert the retrieved data back to the
            desired format.

        Returns:
            The retrieved data as bytes, or None if the key does not
            exist in the cache.
        """
        data = self._redis.get(key)
        if fn is not None and data is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from the Redis cache using the provided key.

        Args:
            key: The key under which the string value is stored in the cache.

        Returns:
            The retrieved string value, or None if the key does not exist in
            the cache.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from the Redis cache using the provided key.

        Args:
            key: The key under which the integer value is stored in the cache.

        Returns:
            The retrieved integer value, or None if the key does not exist
            in the cache.
        """
        return self.get(key, fn=int)
