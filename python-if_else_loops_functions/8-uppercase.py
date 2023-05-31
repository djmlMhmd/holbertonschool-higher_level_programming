#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for i in str:
        char = chr(ord(i) - 32) if 97 <= ord(i) <= 122 else i
        upper = upper + char
    print("{}".format(upper))
