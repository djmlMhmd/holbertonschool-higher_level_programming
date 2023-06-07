#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rank in matrix:
        new_rank = []
        for element in rank:
            new_rank.append(element ** 2)
        new_matrix.append(new_rank)
    return new_matrix