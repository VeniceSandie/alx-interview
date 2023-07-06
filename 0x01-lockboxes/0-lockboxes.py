def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is unlocked initially

    keys = boxes[0]  # Start with the keys from the first box
    while keys:
        key = keys.pop()  # Take a key from the list of keys
        if not unlocked_boxes[key]:
            unlocked_boxes[key] = True  # Unlock the box
            keys.extend(boxes[key])  # Add the keys from the opened box

    return all(unlocked_boxes)
