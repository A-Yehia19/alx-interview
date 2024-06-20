#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """lockboxes function"""
    keys = {0}  # key to first box
    unlocked = set()  # oppened boxes

    while len(keys) > 0:
        key = keys.pop()
        if key < 0 or key >= len(boxes):
            continue

        if key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

        if len(unlocked) == len(boxes):
            return True

    return False
