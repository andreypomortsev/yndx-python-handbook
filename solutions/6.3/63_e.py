import sys

import requests


def get_value(host: str, searching_paths: list) -> int:
    total = 0
    for path in searching_paths:
        response = requests.get(f"http://{host}{path}", timeout=2)
        data = response.json()
        total += sum(data)
    return total


inputs = (arg.strip() for arg in sys.stdin)
server, paths = next(inputs), list(inputs)

sum_of_paths = get_value(server, paths)
print(sum_of_paths)
