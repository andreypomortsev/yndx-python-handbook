def recursive_digit_sum(number: int) -> int:
    number = str(number)
    if len(number) == 1:
        return int(number[0])
    return int(number[0]) + recursive_digit_sum(number[1:])
