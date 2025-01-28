import requests

FIELDS = ("username", "last_name", "first_name", "email")
TIMEOUTS = (3, 5)  # connect, read

host_port = input()
user = dict(zip(FIELDS, [input() for _ in range(4)]))
url_path = f"http://{host_port}/users"

requests.post(url_path, json=user, timeout=TIMEOUTS)
