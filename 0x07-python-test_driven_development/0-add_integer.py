#!/usr/bin/python3
"""Module for defining the add_integer method."""

def add_integer(a, b=98):
    """Return the integer of the addion of a and b.
    Float arguments are typecasted to ints before addition is performaed.

    Raises:
    TypeError: If a, b are not int, float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an inetger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TyperError("b must be an integer")
    return (int(a) + int(b))
