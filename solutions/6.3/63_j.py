import requests

url, user_id = input(), input()
link = f"http://{url}/users/{user_id}"

requests.delete(link, timeout=5)
