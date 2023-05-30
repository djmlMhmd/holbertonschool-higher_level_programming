#!/usr/bin/python3
start, end = -4, 98

for num in range(start, end + 1):

    if num >= 0:
        z = (format(num, '#x'))
        print(f"{num} = {z}")
