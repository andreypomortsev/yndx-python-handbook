def number_length(number: int) -> int:
    if not number:
        return 1

    if number < 0:
        number = -number

    length = 0

    while number > 0:
        length += 1
        number //= 10

    return length
