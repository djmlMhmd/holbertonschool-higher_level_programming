#!/usr/bin/python3
"""List"""


class MyList(list):
    """list and sorted list"""

    def print_sorted(self):
        print(sorted(self))