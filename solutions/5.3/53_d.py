def only_positive_even_sum(a: int, b: int) -> int:
    if not isinstance(b, int) or not isinstance(a, int):
        raise TypeError

    if a < 0 or b < 0 or a % 2 or b % 2:
        raise ValueError

    return a + b
