#!/usr/bin/python3
"""To define a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
