#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    if n == 1:
        return 0  # No operations needed, already have 1 H

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        j = 2
        while j * j <= i:
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)
                operations[i] = min(operations[i], operations[i // j] + j)
            j += 1

    return operations[n] if operations[n] != float('inf') else 0
