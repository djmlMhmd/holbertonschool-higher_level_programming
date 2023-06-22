#!/usr/bin/python3

"""
class MyList
"""

class MyList(list):
    """
    A custom list class.
    """
    def print_sorted(self):
        """
        Print the list in sorted order.
        """
        print(sorted(self))
