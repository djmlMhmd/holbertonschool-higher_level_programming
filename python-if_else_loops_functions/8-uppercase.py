#!/usr/bin/python3

def uppercase(str):

    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            j = 32
        else:
            j = 0
        print("{:c}".format(ord(str[i]) - j), end="")
    print()
