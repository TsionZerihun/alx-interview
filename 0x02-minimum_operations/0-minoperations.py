#!/usr/bin/python3
"""
task0
"""


def minOperations(n):
    """minoperations"""
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
