## [Data merging](../../../solutions/3.5/35_n.py)

A local company is updating user data and decided to reorganize the storage system.

Write a program that updates user data stored in a _JSON_ file.

### Input format

The user enters two file names.\
The first file contains a _JSON_ array of users.\
The second file contains an array of new data.

Information about each user is represented as a _JSON_ object, which must include the field `name`, describing the user's name. Other fields are optional.

### Output format:

Write the user information to the first file in the form of a _JSON_ object, where the keys are the users' names and the values are the objects with their information.

If any additional user information changes, the lexicographically greater value should be preserved.

### Example

__Input__
```plaintext
# User input:
users.json
updates.json

# Contents of the users.json file
[
    {
        "name": "Ann",
        "address": "Flower st."
    },
    {
        "name": "Bob",
        "address": "Summer st.",
        "phone": "+7 (123) 456-78-90"
    }
]

# Contents of the updates.json file
[
    {
        "name": "Ann",
        "address": "Awesome st.",
        "phone": "+7 (098) 765-43-21"
    },
    {
        "name": "Bob",
        "address": "Winter st."
    }
]

```

__Output__
```plaintext
# Contents of the users.json file
{
    "Ann": {
        "address": "Flower st.",
        "phone": "+7 (098) 765-43-21"
    },
    "Bob": {
        "address": "Winter st.",
        "phone": "+7 (123) 456-78-90"
    }
}
```