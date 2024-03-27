#!/usr/bin/env python3
"""
Module: 8-all.py

This module contains a function that lists all documents
in a collection
"""


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    documents = list(mongo_collection.find())
    return documents
