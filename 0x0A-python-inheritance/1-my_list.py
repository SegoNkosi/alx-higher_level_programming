#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements custom sorted printing for the built-in list class."""

    def print_sorted(self):
        """Method for printing a list in sorted ascending order."""
        print(sorted(self))
