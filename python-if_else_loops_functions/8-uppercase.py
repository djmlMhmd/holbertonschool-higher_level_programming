#!/usr/bin/python3

def uppercase(str):

    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            upper_word += chr(ord('A') + (ord(str[i]) - ord('a')))
        else:
            print("{:c}".format(ord(str[i]) - 0), end="")
    print()
