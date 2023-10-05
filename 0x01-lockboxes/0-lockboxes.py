#!/usr/bin/python3
'''LockBoxes'''


def canUnlockAll(boxes):
    '''Returns true if boxes open else false
    '''
    length = len(boxes)
    keys = set()
    unlocked_boxes = []
    i = 0

    while i < length:
        last_i = i
        unlocked_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in unlocked_boxes:
                i = key
                break
        if last_i != i:
            continue
        else:
            break

    for i in range(length):
        if i not in unlocked_boxes and i != 0:
            return False
    return True
