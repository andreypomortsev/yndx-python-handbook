def number_length(number: int) -> int:
    """
    Calculates the length of a given integer via math.
    Which is a low level approach to better understand
    how the length of a number can be calculated.

    Args:
        number (int): The integer to calculate the length of.

    Returns:
        int: The length of the given integer.
    """
    if not number:
        return 1

    if number < 0:
        number = -number

    length = 0

    while number > 0:
        length += 1
        number //= 10

    return length
