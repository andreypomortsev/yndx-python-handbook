## [Data Deletion](../../../solutions/6.3/63_j.py)

Let's conclude the work with the server from previous tasks. A _DELETE_ request to the path _/users/\<id\>_ will delete the user with the specified identifier.

Write a program that deletes a user from the system.

### Input Format

The first line contains the server address.\
The second line contains the identifier of the user whose information needs to be deleted.

### Output Format

No output is required.

### Example

__Input__
```plaintext
# User input:
127.0.0.1:5000
2
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
        "id": 3,
        "username": "third",
        "last_name": "Ivanov",
        "first_name": "Viktor",
        "email": "vik.ivanov@server.none"
    }
]
```