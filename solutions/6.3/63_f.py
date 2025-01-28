import requests


def get_users(url: str) -> list:
    TIMEOUT = 1
    response = requests.get(url, timeout=TIMEOUT)
    users = response.json()

    params = {"key": lambda user: (user["last_name"], user["first_name"])}
    sorted_users = sorted(users, **params)

    return [
        f"{user["last_name"]} {user["first_name"]}" for user in sorted_users
    ]


host_port = input()
url_path = f"http://{host_port}/users"
fl_names = get_users(url_path)
print(*fl_names, sep="\n")
