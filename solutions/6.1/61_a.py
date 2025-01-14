import math


def calculate_expression(x: float | int) -> float:
    part1 = math.log(x ** (3 / 16), 32)
    part2 = x ** (math.cos((math.pi * x) / (2 * math.e)))
    part3 = math.sin(x / math.pi) ** 2
    result = part1 + part2 - part3

    return result


number = float(input())
print(calculate_expression(number))
