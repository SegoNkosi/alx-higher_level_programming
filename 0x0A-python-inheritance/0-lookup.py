#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """Looks up object attributes and methods.
    Args:
        obj (object): the object to list.

    Return a list of an object's available attributes."""
    return (dir(obj))
