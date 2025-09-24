def find_mountains(heights: list) -> list:
    """
    Finds the indices of the mountains in the given list of heights by
    iterating through the list and checking if the current element is
    greater than its neighbors.

    Args:
        heights (list): A list of heights.

    Returns:
        list: A list of indices of the mountains.
    """
    mountains = []

    for i in range(1, len(heights) - 1):
        left = heights[i - 1]
        middle = heights[i]
        rigth = heights[i + 1]
        if left < middle > rigth:
            mountains.append(i + 1)

    return tuple(mountains)
