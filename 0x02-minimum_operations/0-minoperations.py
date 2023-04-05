#!/usr/bin/python3
"""
Task0
"""


def minOperations(n):
    """returns t"""
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t