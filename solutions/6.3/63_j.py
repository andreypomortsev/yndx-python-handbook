import requests

TIMEOUT = 5
host_port = input()
user_id = input()

url_path = f"http://{host_port}/users/{user_id}"

requests.delete(url_path, timeout=TIMEOUT)
