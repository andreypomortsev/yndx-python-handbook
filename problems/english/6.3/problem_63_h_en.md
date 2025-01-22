## [New User Registration](../../../solutions/6.3/63_h.py)

Let's continue working with the server from previous tasks. A _POST_ request to the path _/users_ allows the creation of new users. The request body (`data`) must contain a _JSON_ object with user information (without specifying the identifier).

Write a program that adds a new user to the system.

### Input Format

The first line contains the server address.\
The next lines contain: the username, last name, first name, and email address.

### Output Format

No output is required.

### Example

__Input__
```plaintext
# User input:
127.0.0.1:5000
fourth
Petrov
Kirill
k.petrov@server.none
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
    },
    {
        "username": "fourth",
        "last_name": "Petrov",
        "first_name": "Kirill",
        "email": "k.petrov@server.none",
        "id": 4
    }
]
```