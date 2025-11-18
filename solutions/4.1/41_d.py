def take_small(numbers: list) -> list:
    """
    Filters out numbers greater than or equal to 100 from the given list.

    Args:
        numbers (list): The list of numbers to filter.

    Returns:
        list: A new list containing only numbers less than 100.
    """
    filtered_numbers = []

    for number in numbers:
        if number < 100:
            filtered_numbers.append(number)

    return filtered_numbers
