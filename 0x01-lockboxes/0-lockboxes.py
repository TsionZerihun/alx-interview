#!/usr/bin/python3
"""
task0:canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Returns boolean
    """
    keys = set()

    for box_id, box in enumerate(boxes):
        if len(box) == 0 or box_id == 0:
            keys.add(box_id)
        for key in box:
            if key < len(boxes) and key != box_id:
                keys.add(key)
        if len(keys) == len(boxes):
            return True
    return False