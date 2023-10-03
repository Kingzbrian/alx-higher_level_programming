#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = []
    for x in matrix:
        r.append(list(map(lambda x: x**2, x)))
    return (r)
