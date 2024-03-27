#!/usr/bin/env python3
""" 11-schools_by_topic.py """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic."""
    filter_query = {'topics': topic}
    return (mongo_collection.find(filter_query))
