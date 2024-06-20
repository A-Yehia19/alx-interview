#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """lockboxes function"""
    keys = {0}  # key to first box
    unlocked = set()  # oppened boxes

    while len(keys) > 0:
        key = keys.pop()

        if key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

        if len(unlocked) == len(boxes):
            return True

    return False


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
