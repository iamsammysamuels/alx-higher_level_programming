#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        len_row = len(row)
        for col in range(0, len_row):
            if col != (len_row - 1):
                print("{:d}".format(row[col]), end=' ')
            else:
                print("{:d}".format(row[col]), end='')
        print()
