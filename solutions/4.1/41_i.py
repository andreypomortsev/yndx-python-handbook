def is_prime(n: int) -> bool:
    """
    Проверяет, является ли заданное число простым.

    Аргументы:
        n (int): Число для проверки на простоту.

    Возвращает:
        bool: True — если переданное число простое, а иначе — False.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    sqrt = int(n**0.5) + 1

    while i < sqrt:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
