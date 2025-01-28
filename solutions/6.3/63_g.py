import sys

import requests


def get_user(server: str, text: str) -> str:
    TIMEOUT = 1
    response = requests.get(server, timeout=TIMEOUT)

    if not response.ok:
        return "Пользователь не найден"

    user = response.json()
    return text.format(**user)


host_port = sys.stdin.readline().strip()
user_id = sys.stdin.readline().strip()
message = sys.stdin.read()

url_path = f"http://{host_port}/users/{user_id}"
clean_message = get_user(url_path, message)

print(clean_message)
