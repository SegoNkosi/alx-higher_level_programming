#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(tuple_b=(), tuple_c=()):
    """To add two tuples."""
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    if len(tuple_c) < 2:
        if len(tuple_c) == 0:
            tuple_c = 0, 0
        else:
            tuple_c = tuple_c[0], 0

    return (tuple_b[0] + tuple_c[0], tuple_b[1] + tuple_c[1])
