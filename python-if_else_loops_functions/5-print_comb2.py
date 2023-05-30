#!/usr/bin/python3
for num in range(99 + 1):
    if num < 99:
        print("{:02d}".format(num), end=', ')
else:
    print("{}".format(num))
