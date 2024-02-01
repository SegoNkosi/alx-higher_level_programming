#!/usr/bin/python3
"""Define a class that is locked."""

class LockedClass:
    """
    Prevents the user from instatntiating new LockedClass attributes
    for anything but attributes are called 'first_name'.
    """

    __slots__ = ["first_name"]
