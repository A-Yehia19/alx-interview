#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate matrix"""
    n = len(matrix)
    tmp_matrix = [[-1] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            tmp_matrix[x][y] = matrix[n-y-1][x]

    matrix[:] = tmp_matrix
