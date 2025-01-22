import requests


def get_users(url: str) -> list:
    response = requests.get(url, timeout=1)
    users = response.json()

    params = {"key": lambda user: (user["last_name"], user["first_name"])}
    sorted_users = sorted(users, **params)

    return [
        f"{user["last_name"]} {user["first_name"]}" for user in sorted_users
    ]


url = input()
server = f"http://{url}/users"
fl_names = get_users(server)
print(*fl_names, sep="\n")
