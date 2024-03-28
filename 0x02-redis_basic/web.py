#!/usr/bin/env python3
"""
Module to fetch HTML content of a URL and cache the result with an
expiration time of 10 seconds.
"""

import requests
import redis
import time


def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and caches the result with an
    expiration time of 10 seconds.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Initialize Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Increment access count for the URL
    count_key = f"count:{url}"
    r.incr(count_key)

    # Check if the content is cached
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch HTML content from the URL
    response = requests.get(url)
    content = response.text

    # Cache the content with an expiration time of 10 seconds
    r.setex(url, 10, content)

    return content
