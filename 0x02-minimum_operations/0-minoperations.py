#!/usr/bin/python3
"""Minimum Operations function module."""


def minOperations(n):
    """Minimum Operations function."""
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if remainder % now == 0:
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
