## [Specific Value](../../../solutions/6.3/63_d.py)

The server responds to the request with a _JSON_ object.\
Output the value located in the object by the given key.\
If such a value is not found, output the message "No data".

### Input Format

The first line contains the server address. The second line contains the key name.

### Output Format

One line — the value obtained from the given key, or the message "No data".

### Example 1

__Input__
```plaintext
# User input:
127.0.0.1:5000
second
# Server data:
{"first": "1", "second": "2"}
```

__Output__
```plaintext
2
```

### Example 2

__Input__
```plaintext
# User input:
127.0.0.1:8080
second
# Server data:
{"first": "1", "third": "3"}
```

__Output__
```plaintext
No data
```