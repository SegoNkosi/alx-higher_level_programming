#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for j in sorted(a_dictionary.keys()):
        print("{}:{}".format(j, a_dictionary.get(j)))
