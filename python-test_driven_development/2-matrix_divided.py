#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix(int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix == div:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
