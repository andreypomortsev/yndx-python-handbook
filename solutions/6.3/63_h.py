import requests

FIELDS = ("username", "last_name", "first_name", "email")

url = input()
user = dict(zip(FIELDS, [input() for _ in range(4)]))

requests.post(f"http://{url}/users", json=user, timeout=(3, 5))
