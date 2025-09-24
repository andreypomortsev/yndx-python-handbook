def split_numbers(numbers: str) -> tuple:
    """
    Splits a string of space-separated numbers into a tuple of integers.
    Will fail miserably if one of the symbols is not an integer.

    Args:
        numbers (str): A string of space-separated numbers.

    Returns:
        tuple: A tuple of integers.
    """
    return tuple(map(int, numbers.split()))
