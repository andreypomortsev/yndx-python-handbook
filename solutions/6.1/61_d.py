import math
import sys


def geometric_mean(numbers: list) -> float:
    product = math.prod(numbers)
    n = len(numbers)
    return math.pow(product, 1 / n)


nums = list(map(float, sys.stdin.read().split(" ")))
print(geometric_mean(nums))
