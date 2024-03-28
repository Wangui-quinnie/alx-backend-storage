#!/usr/bin/env python3
"""
Cache module
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


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

    def count_calls(method: Callable) -> Callable:
        """Decorator to count the number of times a method is called.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """Wrapper function to count method calls and invoke the original
            method.

            Args:
                self: The Cache instance.
                *args: Positional arguments passed to the method.
                **kwargs: Keyword arguments passed to the method.

            Returns:
                The result of the original method call.
            """
            key = f"method:{method.__qualname__}"
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """Decorator to store the history of inputs and outputs for a function.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """Wrapper function to store input and output history in Redis.

            Args:
                self: The Cache instance.
                *args: Positional arguments passed to the method.
                **kwargs: Keyword arguments passed to the method.

            Returns:
                The result of the original method call.
            """
            self._redis.rpush(method.__qualname__ + ":all_inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(result))
        return result
    return wrapper

    def replay(fn: Callable):
        """Display the history of calls of a particular function."""
        r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    # print(f"{function_name} was called {value} times")
    print("{} was called {} times:".format(function_name, value))
    # inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)

    # outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        # print(f"{function_name}(*{input}) -> {output}")
        print("{}(*{}) -> {}".format(function_name, input, output))

    @call_history
    @count_calls
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

    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes,
                                                    int, float]:
        """
        method that take a key string argument and an
        optional Callable argument named fn. This callable will be used
        to convert the data back to the desired format
        """
        if not self._redis.exists(key):
            return None
        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """
        Method that converts the data back into a string
        """
        if not self._redis.exists(key):
            return None
        return str(self._redis.get(key))

    def get_int(self, key):
        """Method used to convert data back into an int"""
        if not self._redis.exists(key):
            return None
        return int.from_bytes(self._redis.get(key), "big")
