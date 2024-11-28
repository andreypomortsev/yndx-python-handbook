import json

DEFAULT_ENCODING = {"encoding": "UTF-8"}

users_file = input()
updates_file = input()

with (
    open(users_file, "r+", **DEFAULT_ENCODING) as file_one,
    open(updates_file, "r", **DEFAULT_ENCODING) as file_two,
):
    users = json.load(file_one)
    updates = json.load(file_two)

    users += updates
    updated_users = {}

    for user in users:
        name = user["name"]
        updated_users[name] = updated_users.get(name, {})
        for key, value in user.items():
            if key != "name":
                flag = updated_users[name].get(key, "")
                if flag < value:
                    updated_users[name][key] = value

    file_one.seek(0)
    json.dump(updated_users, file_one, ensure_ascii=False, indent=4)
    file_one.truncate()
