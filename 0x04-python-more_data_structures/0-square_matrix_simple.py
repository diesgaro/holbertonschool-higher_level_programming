#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(list(map(lambda x: x**2, subm)) for subm in matrix)
    return new_matrix
