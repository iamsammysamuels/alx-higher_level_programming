#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
        Executes the square value of all integers of a matrix
    """
    return ([[m**2 for m in row] for row in matrix])
