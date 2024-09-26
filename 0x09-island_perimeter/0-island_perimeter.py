#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with 4 edges
                perimeter += 4
                # Check if there's land above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                # Check if there's land below
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                # Check if there's land to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                # Check if there's land to the right
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
