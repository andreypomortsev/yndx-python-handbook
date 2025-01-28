import sys

import requests


def get_value(host: str, searching_paths: list) -> int:
    TIMEOUT = 2
    total = 0
    for path in searching_paths:
        url_path = f"http://{host}{path}"
        response = requests.get(url_path, timeout=TIMEOUT)
        data = response.json()
        total += sum(data)
    return total


inputs = (arg.strip() for arg in sys.stdin)
host_port, paths = next(inputs), list(inputs)

sum_of_paths = get_value(host_port, paths)
print(sum_of_paths)
