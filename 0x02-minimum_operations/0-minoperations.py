#!/usr/bin/python3
"""
    A method that determines the min number required of
    operations to achieve exactly n H characters in the file.
"""


def minOperations(n):
    """
        A function that calculates the min  number of operations
        needed to produce n H characters in a file
    """
    n_0 = 1
    start = 0
    index = 0
    while n_0 < n:
        rest = n - n_0
        if (rest % n_0 == 0):
            start = n_0
            n_0 += start
            index += 2
        else:
            n_0 += start
            index += 1
    return index
