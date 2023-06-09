#!/usr/bin/python3
def roman_to_int(roman_string):
    romain_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if roman_string is None or not isinstance(roman_string, str):
        return num
    for i in range(len(roman_string)):
        current_val = romain_num[roman_string[i]]
        if i > 0:
            prev_val = romain_num[roman_string[i - 1]]
            if current_val > prev_val:
                num += current_val - 2 * prev_val
            else:
                num += current_val
        else:
            num += current_val
    return num
