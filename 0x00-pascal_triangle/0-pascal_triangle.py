#!/usr/bin/python3
"""
task 0: that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    Return list of lists of ints
    """
    if n <= 0:
        return []

    pasTriangle = [[1]]

    for row in range(2, n + 1):
        rows = []

        for idx in range(row):
            if idx == 0 or idx == row - 1:
                rows.append(1)
                continue
            value = pasTriangle[row - 2][idx] + pasTriangle[row - 2][idx - 1]
            rows.append(value)

        pasTriangle.append(rows)

    return pasTriangle