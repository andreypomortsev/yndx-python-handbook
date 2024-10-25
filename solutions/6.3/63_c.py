import requests


def get_server_sum(url: str) -> int:
    total = 0
    response = requests.get(url, timeout=1)
    numbers = response.json()

    for number in numbers:
        if isinstance(number, (int, float)):
            total += number

    return total


server = f"http://{input()}"
sum_of_responses = get_server_sum(server)

print(sum_of_responses)
