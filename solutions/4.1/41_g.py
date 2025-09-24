def max2D(matrix: list) -> int:
    """
    A low level representation of a max2D function.
    The time complexity of this function is O(n^2) and cannot be reduced,
    because we need to check every element in the matrix.
    The space complexity of this function is O(1),
    because we only use a constant amount of extra space.

    Args:
        matrix (list): The 2D list to search.

    Returns:
        int: The maximum value found in the 2D list.
    """
    maximum = float("-inf")

    for row in matrix:
        for number in row:
            if number > maximum:
                maximum = number

    return maximum
