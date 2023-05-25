#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n H characters in the file."""
    if n <= 1:
        return 0
    
    character = 1
    copy = character 
    min_ops = 0

    while character < n:
        if n%character == 0:
            copy = character
            min_ops += 2
        else:
            min_ops += 1
        return min_ops
