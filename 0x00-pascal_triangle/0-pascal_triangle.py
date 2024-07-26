#!/usr/bin/python3
"""Generate Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a specified number of rows (n).

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle,
        or an empty list if n <= 0.
    """
    if n <= 0:
        # If n is not positive, return an empty list
        return []

    triangle = [[1]]
    # The first row of Pascal's triangle is always [1]

    for i in range(1, n):
        # For each subsequent row, start with 1
        row = [1]

        # Compute the middle values based on the previous row
        previous_row = triangle[i - 1]
        for j in range(1, i):
            # Each middle value is the sum of the two values above it
            row.append(previous_row[j - 1] + previous_row[j])
            # End the row with 1
        row.append(1)
        # Append the newly created row to the triangle
        triangle.append(row)

    return triangle
