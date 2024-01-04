#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfunc = dir()
    for k in range(0, len(allfunc))
     if allfunc[k][:2] != "__":
         print("{:s}".format(allfunc[k]))
