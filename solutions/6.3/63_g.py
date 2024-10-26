import sys

import requests


def get_user(server: str, text: str) -> str:
    response = requests.get(server, timeout=1)

    if not response.ok:
        return "Пользователь не найден"

    user = response.json()
    return text.format(**user)


url = sys.stdin.readline().strip()
user_id = sys.stdin.readline().strip()
message = sys.stdin.read()

clean_message = get_user(f"http://{url}/users/{user_id}", message)

print(clean_message)
