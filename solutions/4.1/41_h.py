def normilize_input(input_value: str) -> str | list:
    """
    Нормализует данные.

    Аргументы:
        input_value (str | int | tuple | list): Входящие данные
            для нормализации.

    Возвращает:
        str: Нормализованные данные.
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
    Проверяет, является ли входное значение палиндромом.

    Аргументы:
        input_value (str | int | tuple | list): Входное значение для проверки
            на палиндром.

    Возвращает:
        bool: True, если входное значение является палиндромом, иначе False.
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
