#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to store data in Redis
    """

    def __init__(self) -> None:
        """
        Initialize the Cache instance with a Redis client
        """
        self._redis: redis.Redis = redis.Redis()
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
