## [Summing Responses 2](../../../solutions/6.3/63_c.py)

The server responds to the request with a _JSON_ list.  
Output the sum of the numbers in the received list.

### Input Format

The server address is provided.

### Output Format

A single number — the sum of all numbers in the received list.

### Example 1

__Input__
```plaintext
# User input:
127.0.0.1:5000
# Server data:
[1, 2, "error", 3]
```

__Output__
```plaintext
6
```

### Example 2

__Input__
```plaintext
# User input:
127.0.0.1:8080
# Server data:
[7, 3, ["error"], -5, 2]
```

__Output__
```plaintext
7
```