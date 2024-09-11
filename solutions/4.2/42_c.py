def gcd(*numbers) -> int:
    if len(numbers) < 2:
        return numbers[0] if numbers else None

    a = numbers[0]

    for b in numbers[1:]:
        while b:
            a, b = b, a % b

    return a
