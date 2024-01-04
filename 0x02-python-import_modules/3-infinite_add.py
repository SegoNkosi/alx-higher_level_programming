#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    for j in range(1, len(argv)):
        sumint += int(argv[j])
    print("{}".format(sumint))
