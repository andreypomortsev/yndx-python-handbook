import requests

response = requests.get("http://127.0.0.1:5000", timeout=1)
print(response.text)
