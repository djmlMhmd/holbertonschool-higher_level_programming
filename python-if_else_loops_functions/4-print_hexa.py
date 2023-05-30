#!/usr/bin/python3

for num in range(0, 98 + 1):

    if num >= 0:
        hexa = (format(num, '#x'))
        print(f"{num} = {hexa}")
