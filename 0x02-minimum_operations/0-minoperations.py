#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations to reach n characters in a text file"""
    res = 0
    i = 2
    while i <= n:
        while n % i == 0:
            res += i
            n = n // i
        i += 1
    return res
