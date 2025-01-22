## [Summing Responses](../../../solutions/6.3/63_b.py)

Write a program that sums the data transmitted from the server.

If the server sends the number 0, it means the data has finished, and it will restart the response output.

### Input Format

The server address is provided.

### Output Format

A single number — the sum of all data received from the server.

### Example 1

__Input__
```plaintext
# User input:
127.0.0.1:5000
# Server data:
1
2
3
0
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
7
3
-5
2
0
```

__Output__
```plaintext
7
```