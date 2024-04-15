def canUnlockAll(boxes):
    # Initialize a set to keep track of keys we have
    keys = {0}  # Start with the key to the first box

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Iterate over boxes until no new keys can be found
    while keys:
        # Pop a key from the set of keys
        key = keys.pop()

        # Add the current box to visited
        visited.add(key)

        # Add any new keys found in the current box to the set of keys
        keys |= set(boxes[key])

        # Remove any keys that open boxes we have already visited
        keys -= visited

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
