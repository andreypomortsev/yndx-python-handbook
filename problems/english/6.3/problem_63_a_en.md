## [System Check](../../../solutions/6.3/63_a.py)

A server _127.0.0.1_ is running on the local network of the testing system. It listens on port _5000_ and occasionally responds to it.

Connect to the server and output the message received from it.

### Notes

All tasks in this chapter use the _http_ protocol.\
Remember that the server's response is a binary object and should be decoded.

### Example 1

__Input__
```plaintext
# User input:

# Server data:
Hello!
```

__Output__
```plaintext
Hello!
```

### Example 2

__Input__
```plaintext
# User input:

# Server data:
The server is operating normally
```

__Output__
```plaintext
The server is operating normally
```