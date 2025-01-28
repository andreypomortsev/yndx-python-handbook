## [Put Yourself in My Shoes](../../../solutions/3.5/35_o.py)

You have been solving problems in Yandex.Contest for a long time.\
Today, it's time to feel what it's like to be in its place.

Write a small testing system.

Your solution has access to a file _scoring.json_, which contains information about the testing system.

The core of the system is a list of test groups.\
Each group is an object with the following fields:

- _points_ — the number of points that can be earned for passing this group;
- _tests_ — a list of objects describing individual tests.
An object describing a test contains the following fields:

- _input_ — the input data string for the test;
- _pattern_ — the expected answer string.

The answers received from the tested program are passed to the standard input stream of your solution.

### Input format

Strings containing the answers from the tested program for each test are passed to the standard input stream.\
The _scoring.json_ file contains information about the tests for the task.

### Output format:

One number — the score received by the tested program.\
If a test group was not passed fully, a proportional score is given for that group.\
It is guaranteed that the points for a group are divisible by the number of tests in it.

### Example

__Input__
```plaintext
# User input:
4
12
3
100
0

# Contents of the scoring.json file
[
    {
        "points": 10,
        "tests": [
            {
                "input": "2 2",
                "pattern": "4"
            },
            {
                "input": "4 3",
                "pattern": "7"
            }
        ]
    },
    {
        "points": 30,
        "tests": [
            {
                "input": "2 1",
                "pattern": "3"
            },
            {
                "input": "25 4",
                "pattern": "29"
            },
            {
                "input": "3 -3",
                "pattern": "0"
            }
        ]
    }
]
```

__Output__
```plaintext
25
```