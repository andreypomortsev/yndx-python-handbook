import math


def get_chanses(n: int, m: int) -> tuple:
    all_options = math.comb(n, m)
    vasya_in_options = all_options * m // n

    return vasya_in_options, all_options


guests, seats = map(int, input().split())
answer = get_chanses(guests, seats)
print(*answer)
