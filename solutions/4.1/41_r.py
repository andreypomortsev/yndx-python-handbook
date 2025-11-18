def merge(left: tuple, right: tuple) -> tuple:
    """
    Merges two sorted tuples into one sorted tuple.

    Args:
        left (tuple): The first sorted tuple.
        right (tuple): The second sorted tuple.

    Returns:
        tuple: The merged sorted tuple.
    """
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return tuple(merged)
