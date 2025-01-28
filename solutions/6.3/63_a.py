import requests

URL = "http://127.0.0.1:5000"
TIMEOUT = 1

response = requests.get(URL, timeout=TIMEOUT)
print(response.text)
