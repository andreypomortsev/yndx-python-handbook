## [User List](../../../solutions/6.3/63_f.py)

On the server, at the path _/users_, a list of users is available, represented as _JSON_ objects with the following keys:

- `id` — unique identifier of the user;
- `username` — username;
- `last_name` — last name;
- `first_name` — first name;
- `email` — email address.

### Input Format

The first line contains the server address.

### Output Format

Output the list of all users in alphabetical order.

### Example

__Input__
```plaintext
# User input:
127.0.0.1:5000
# Server data:
[
    {
        "id": 1,
        "username": "first",
        "last_name": "Petrova",
        "first_name": "Elizaveta",
        "email": "e.petrova@server.none"
    },
    {
        "id": 2,
        "username": "second",
        "last_name": "Ivanov",
        "first_name": "Vasily",
        "email": "vas.ivanov@server.none"
    },
    {
        "id": 3,
        "username": "third",
        "last_name": "Ivanov",
        "first_name": "Viktor",
        "email": "vik.ivanov@server.none"
    }
]
```

__Output__
```plaintext
Ivanov Vasily
Ivanov Viktor
Petrova Elizaveta
```