#!/usr/bin/python3
"""Island Perimeter"""


def expand_island(grid, row, col):
    """expand the island"""
    up = 0 if row - 1 < 0 else grid[row - 1][col]
    down = 0 if row + 1 < len(grid) else grid[row + 1][col]
    left = 0 if col - 1 < 0 else grid[row][col - 1]
    right = 0 if col + 1 < len(grid[0]) else grid[row][col + 1]

    grid[row][col] = -1
    count = [up, down, left, right].count(0)

    if up == 1:
        count += expand_island(grid, row - 1, col)
    if down == 1:
        count += expand_island(grid, row + 1, col)
    if left == 1:
        count += expand_island(grid, row, col - 1)
    if right == 1:
        count += expand_island(grid, row, col + 1)

    return count


def island_perimeter(grid):
    """find the perimeter of island"""
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter = expand_island(grid, row, col)
                return perimeter

    return perimeter
