## [Changing User Data](../../../solutions/6.3/63_i.py)

Let's continue with the server from previous tasks. A _PUT_ request to the path _/users/\<id\>_ allows updating the user information. To do this, a _JSON_ object containing the new information (without the identifier) needs to be sent in the request data (`data`).

Write a program that updates the user's information.

### Input Format

The first line contains the server address.\
The second line contains the identifier of the user whose information needs to be updated. The following lines contain the fields to be updated in the format: `<field_name>=<new_value>`.

### Output Format

No output is required.

### Example

__Input__
```plaintext
# User input:
127.0.0.1:5000
2
username=ivanov_vasily
email=ivanov_vasily@server.none
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
        "username": "ivanov_vasily",
        "last_name": "Ivanov",
        "first_name": "Vasily",
        "email": "ivanov_vasily@server.none"
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