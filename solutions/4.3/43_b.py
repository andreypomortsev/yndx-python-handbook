def recursive_digit_sum(number: int) -> int:
    if number < 10:
        return number
    return (number % 10) + recursive_digit_sum(number // 10)
