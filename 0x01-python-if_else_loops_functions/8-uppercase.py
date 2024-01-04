#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        tempo = iterator
        if ord(tempo) >= 97 and ord(tempo) <= 122:
            temp = chr(ord(iterator) -32)
            print("{}".format(temp), end='')
        print()
