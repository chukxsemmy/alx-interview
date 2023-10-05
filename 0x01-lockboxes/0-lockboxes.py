#!/usr/bin/python
"""LockBoxes Task"""

def canUnlockAll(boxes):
    """
    Returns: True if boxes can open otherwise False
    """
    length = len(boxes)
    stack = [0]
    opened_box = [1] + [0] * (length - 1)
    i = 0

    if length == 0:
        return True
    while stack:
        j = stack.pop()
        for index in boxes[j]:
            if index > 0 and index < lenght and opened_box[index] == 0:
                opened_box[index] = 1
                stack.append(index)
        i = i + 1
    if 0 in opened_box:
        return False
    return True
