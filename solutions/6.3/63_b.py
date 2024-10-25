import requests


def get_server_sum(url: str) -> int:
    total = 0
    while True:
        response = requests.get(url, timeout=1)
        number = response.text.strip()
        if number == "0":
            return total
        total += int(number)


url = input()
server = f"http://{url}"
sum_of_responses = get_server_sum(server)

print(sum_of_responses)
