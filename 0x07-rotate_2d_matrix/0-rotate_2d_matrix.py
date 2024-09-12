#!/usr/bin/python3
"""Rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    :param matrix: list of lists (n x n matrix)
    """
    n = len(matrix)
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
