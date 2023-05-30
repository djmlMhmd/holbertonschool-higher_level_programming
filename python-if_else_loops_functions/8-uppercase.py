#!/usr/bin/python3

def uppercase(str):
    upper_word = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            upper_word += chr(ord('A') + (ord(str[i]) - ord('a')))
        else:
            print("{:c}".format(ord(str[i]) - 32), end="")
    print()
