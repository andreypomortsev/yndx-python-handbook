import requests


def get_server_sum(url: str) -> int:
    TIMEOUT = 1
    total = 0
    response = requests.get(url, timeout=TIMEOUT)
    numbers = response.json()

    for number in numbers:
        if isinstance(number, (int, float)):
            total += number

    return total


host_port = input()
url = f"http://{host_port}"
sum_of_responses = get_server_sum(url)

print(sum_of_responses)
