#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if not isinstance(n, int):
        return 0
    count = 0
    clipboard = 0
    paste_copy = 1

    while paste_copy < n:
        if clipboard == 0:
            # first copy all and paste
            clipboard = paste_copy
            paste_copy += clipboard
            count += 2
        elif n - paste_copy > 0 and (n - paste_copy) % paste_copy == 0:
            # copy all and paste
            clipboard = paste_copy
            paste_copy += clipboard
            count += 2
        elif clipboard > 0:
            # paste if clipboard > 0
            paste_copy += clipboard
            count += 1
    return count
