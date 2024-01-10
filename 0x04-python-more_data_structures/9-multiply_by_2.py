#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for j in a_dictionary:
        new_dic[j] = a_dictionary[j] * 2
        return new_dic
