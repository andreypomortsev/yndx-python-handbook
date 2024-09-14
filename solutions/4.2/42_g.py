from typing import Tuple


def enter_results(*pairs) -> Tuple[float]:
    global results

    if "results" in globals():
        results.extend(list(pairs))
    else:
        results = list(pairs)


def get_sum() -> Tuple[float]:
    global results
    global total

    total = list(results[:2])

    for i in range(2, len(results), 2):
        total[i % 2] += results[i]
        total[(i + 1) % 2] += results[i + 1]

    return round(total[0], 2), round(total[1], 2)


def get_average() -> Tuple[float]:
    global results
    global total

    length = len(results) // 2

    return tuple(round(total[i] / length, 2) for i in range(2))
