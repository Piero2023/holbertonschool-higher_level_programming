#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new_matrix = list(map(lambda i: list(map(lambda j: j ** 2, i)), matrix))
    return (new_matrix)
