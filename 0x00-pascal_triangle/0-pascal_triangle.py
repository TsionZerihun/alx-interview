#!/usr/bin/python3
"""
task 0: returns a list of lists of ints
"""


def pascal_triangle(n):
    """
    Returns a list of ints
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        triangle = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            triangle.append(k[i - 1][j] + k[i - 1][j + 1])
        triangle.append(1)
        k.append(triangle)
    return k
