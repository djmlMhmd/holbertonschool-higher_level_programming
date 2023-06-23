#!/usr/bin/python3
"""
representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    function def pascal_triangle(n) that returns a list of lists of integers
    """
    triangle = []
    for i in range(n):
        new_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(new_list)
    return triangle
