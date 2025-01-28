import requests


def get_value(url: str, searching_key: str) -> str:
    TIMEOUT = 1
    response = requests.get(url, timeout=TIMEOUT)
    response_json = response.json()
    return response_json.get(searching_key, "No data")


host_port = input()
key = input()

url = f"http://{host_port}"
json_value = get_value(url, key)

print(json_value)
