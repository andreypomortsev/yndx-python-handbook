def is_palindrome(input_value) -> bool:
    """
    Проверяет, является ли входное значение палиндромом.

    Аргументы:
        input_value (str | int | tuple | list): Входное значение для проверки
            на палиндром.

    Возвращает:
        bool: True, если входное значение является палиндромом,
            False в противном случае.
    """
    if isinstance(input_value, (tuple, list)):
        input_value = list(map(lambda x: str(x).lower(), input_value))

    elif isinstance(input_value, str):
        input_value = "".join(map(lambda x: x.lower(), input_value.split()))

    else:
        input_value = str(input_value)

    return input_value == input_value[::-1]
