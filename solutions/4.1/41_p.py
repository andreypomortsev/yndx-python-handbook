def normilize_input(input_value: str | int | tuple | list) -> str | list:
    """
    Normalizes the input value.

    Args:
        input_value (str | int | tuple | list): The value to normalize.

    Returns:
        str | list: The normalized value.
    """
    if isinstance(input_value, (tuple, list)):
        input_value = list(map(lambda x: str(x).lower(), input_value))

    elif isinstance(input_value, str):
        input_value = input_value.lower()

    else:
        input_value = str(input_value)

    return input_value


def is_palindrome(input_value: str | int | tuple | list) -> bool:
    """
    Checks if the given value is a palindrome.

    Args:
        input_value (str | int | tuple | list): The value to check.

    Returns:
        bool: True if the value is a palindrome, False otherwise.
    """
    symbols = normilize_input(input_value)

    left_index = 0
    right_index = len(symbols) - 1

    while left_index < right_index:
        if symbols[left_index] != symbols[right_index]:
            return False

        left_index += 1
        right_index -= 1

    return True
