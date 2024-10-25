import requests


def get_value(url: str, searching_key: str) -> str:
    response = requests.get(url, timeout=1)
    response_json = response.json()
    return response_json.get(searching_key, "No data")


url_port = input()
key = input()

server = f"http://{url_port}"
json_value = get_value(server, key)

print(json_value)
