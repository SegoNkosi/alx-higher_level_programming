#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replaces an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [y for y in my_list]
    copy[idx] = element
    return (copy)
