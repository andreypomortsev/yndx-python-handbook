## [Message mailing](../../../solutions/6.3/63_g.py)

Let's continue working with the server from the previous task. At the path _/users/\<id\>_, a _JSON_ object of the user with the specified _id_ is available.

Prepare a letter text for sending an important newsletter.

If the user with the specified identifier is not found, output the message "User not found".

### Input Format

The first line contains the server address.\
The second line contains the _id_ of the user to whom the letter should be sent.\
The following lines contain the message content with formatted inserts for any of the object fields.

### Output Format

Output the prepared message.

### Example 1

__Input__
```plaintext
# User input:
127.0.0.1:5000
2
Message for: {email}
Hello, {last_name} {first_name}
We are pleased to inform you about an upcoming promotion!
All the details are on our website
Best regards, the test server team!
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
Message for: vas.ivanov@server.none
Hello, Ivanov Vasily
We are pleased to inform you about an upcoming promotion!
All the details are on our website
Best regards, the test server team!
```

### Example 2

__Input__
```plaintext
# User input:
127.0.0.1:5000
2
Message for: {email}
Hello, {last_name} {first_name} ({username})
We are pleased to inform you about an upcoming promotion!
All the details are on our website
Best regards, the test server team!
# Server data:
[
    {
        "id": 1,
        "username": "first",
        "last_name": "Petrova",
        "first_name": "Elizaveta",
        "email": "e.petrova@server.none"
    }
]
```

__Output__
```plaintext
User not found
```