#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = sys.argv[1:]

num_args = len(args)

if num_args == 0:
        print("{:d} arguments.".format(num_args))
elif num_args == 1:
        print("{:d} argument.".format(num_args))
else:
        print("{:d} arguments.".format(num_args))

if num_args >= 1:
    for arg in sys.argv:
        if num_args != 0:
            print("{:d}: {:s}".format(num_args, arg))
        num_args += 1