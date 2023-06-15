#!/usr/bin/python3
"""
Prototype: def rain(walls)
walls is a list of non-negative integers.
Return: Integer indicating total amount of rainwater retained.
Assume that the ends of the list (before index 0 and after index walls[-1]) are
not walls, meaning they will not retain water.
If the list is empty return 0.
"""


def rain(walls):
    if len(walls) < 3:
        return 0

    total_water = 0
    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            total_water += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            total_water += right_max - walls[right]
            right -= 1

    return total_water
