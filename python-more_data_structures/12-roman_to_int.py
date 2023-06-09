#!/usr/bin/python3
def roman_to_int(roman_string):
    romain_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)-1, -1, -1):
        if i < len(roman_string)-1 and romain_num[roman_string[i]] < romain_num[roman_string[i+1]]:
            num -= romain_num[roman_string[i]]
        else:
            num += romain_num[roman_string[i]]
    return num
