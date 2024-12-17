import cmath
import math


def calculate_expression(x: float | int) -> float:
    part1 = cmath.log(x ** (3 / 16), 32)
    part2 = x ** (cmath.cos((math.pi * x) / (2 * math.e)))
    part3 = cmath.sin(x / math.pi) ** 2
    result = part1 + part2 - part3

    return result.real


number = float(input())
print(calculate_expression(number))
