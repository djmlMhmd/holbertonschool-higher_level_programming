#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        with open(filename, "w", encoding='utf-8') as f:
            return f.write(text)
