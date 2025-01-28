import requests


def get_server_sum(url: str) -> int:
    TIMEOUT = 1
    total = 0
    while True:
        response = requests.get(url, timeout=TIMEOUT)
        number = response.text.strip()
        if number == "0":
            return total
        total += int(number)


host_port = input()
url = f"http://{host_port}"
sum_of_responses = get_server_sum(url)

print(sum_of_responses)
