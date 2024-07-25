#!/usr/bin/python3
"""pascal"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a specified number of rows (n).

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists representing
        Pascal's triangle, or an empty list if n <= 0.
    """
    if n <= 0:
        """Returns an empty list"""
        return []

    triangle = [[1]]
    """Row ends is 1"""

    for i in range(1, n):
        """requirem"""
        row = [1]
        """Each row starts with 1
        Compute the middle values based on the previous row"""
        previous_row = triangle[i - 1]
        for j in range(1, i):
            """Traversal"""
            row.append(previous_row[j - 1] + previous_row[j])
            """End row wirth 1"""
        row.append(1)
        triangle.append(row)

    return triangle
