#!/usr/bin/python3

def uppercase(str):

    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            i = 32
        else:
            i = 0
        print("{:c}".format(ord(str[i]) - 0), end="")
    print()
