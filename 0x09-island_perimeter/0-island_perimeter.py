#!/usr/bin/python3
"""Island Perimeter"""


def expand_island(grid: list[list[int]], row: int, col: int) -> int:
    """expand the island"""
    up = grid[row - 1][col]
    down = grid[row + 1][col]
    left = grid[row][col - 1]
    right = grid[row][col + 1]

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


def island_perimeter(grid: list[list[int]]) -> int:
    """find the perimeter of island"""
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter = expand_island(grid, row, col)
                return perimeter

    return perimeter
