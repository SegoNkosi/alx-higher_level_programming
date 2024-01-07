#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tempo = my_list[:]
    if idx < 0:
        return tempo
    if idx > len(my_list) - 1:
        return tempo
    tempo[idx] = element
    return tempo
