#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    This function determines if all boxes can be
    unlocked by following a set of keys.

    The function operates as follows:
    1. It initializes a set of keys with the key
        from the first box (box0).
    2. It then iterates through the keys in the set,
        using each key to unlock a box.
    3. For each unlocked box, it retrieves all keys
        from that box and adds them to the set of keys to unlock.
    4. This process continues until no new keys
        can be added to the set,
        indicating that all boxes have been unlocked.
    5. The function tracks the number of boxes
        unlocked and compares it to the total number of boxes.
        If the count matches the total,
        it means all boxes have been successfully unlocked.

    Parameters:
        boxes (list): A list of lists,
        where each sublist represents a box
        and contains the keys that can unlock it.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Note:
        - The function assumes that the first box (box0)
            can be unlocked with the key 0.
        - Keys that do not correspond to a box are ignored.
        - The optimization idea mentioned
            (adding 0 to setofkeys at start)
            is already implemented in the function's logic.
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
