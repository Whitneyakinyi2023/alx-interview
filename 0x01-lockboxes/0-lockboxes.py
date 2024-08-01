#!/usr/bin/python3
"""Can unlock all method"""


def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = set([0])  # Start with box 0 unlocked
    keys = [0]  # Initialize with keys from box 0

    while keys:
        key = keys.pop()  # Take the next key to process
        for new_key in boxes[key]:  # Get the keys from the current box
            # If the box has not been unlocked and is a valid box number
            if new_key not in unlocked and new_key < n:
                unlocked.add(new_key)  # Mark the box as unlocked
                keys.append(new_key)  # Add the new key to process

    # Check if the number of unlocked boxes matches the total number of boxes
    return len(unlocked) == n
