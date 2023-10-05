#!/usr/bin/python
"""LockBoxes Task"""


def canUnlockAll(boxes):
    """checks if boxes can be opened
    Returns:
        True: if all boxes open
        False: otherwise
    """
    length = len(boxes)
    keys = set()
    openedBoxes = []
    i = 0

    while i < length:
        newPos = i
        openedBoxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in openedBoxes:
                i = key
                break
        if newPos != i:
            continue
        else:
            break

    for i in range(length):
        if i not in openedBoxes and i != 0:
            return False
    return True
