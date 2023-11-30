#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def boundary_check(grid, i, j):
    """
    check boundary
    """
    mask = 1
    top = grid[i - 1][j] ^ mask if i > 0 else 1
    bottom = grid[i + 1][j] ^ mask if i < (len(grid) - 1) else 1
    left = grid[i][j - 1] ^ mask if j > 0 else 1
    right = grid[i][j + 1] ^ mask if j < (len(grid[i]) - 1) else 1
    positions = top + bottom + right + left
    return positions


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a given grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += boundary_check(grid, i, j)

    return perimeter
