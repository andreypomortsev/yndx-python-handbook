## [Summing Responses 3](../../../solutions/6.3/63_e.py)

The server responds to several paths, each returning its own _JSON_ list. Write a program that collects and sums all the data from the given paths.

### Input Format

The server address and a list of paths to analyze are provided.

### Output Format

A single number — the sum of all numbers from the obtained lists.

### Example 1

__Input__
```plaintext
# User input:
127.0.0.1:5000
/first
/third
# Server data:
/first -> [1, 2, 3]
/second -> [2, 4, 6]
/third -> [3, 6, 9]
```

__Output__
```plaintext
24
```

### Example 2

__Input__
```plaintext
# User input:
127.0.0.1:8080
/second
# Server data:
/first -> [1, 2, 3]
/second -> [2, 4, 6]
/third -> [3, 6, 9]
```

__Output__
```plaintext
12
```