## [Data Preparation](../../../solutions/4.2/42_e.py)

Write a function `to_string` that converts a sequence of data into a string. The function should accept:

- an indefinite number of arguments;
- an optional parameter `sep` (default is a space);
- an optional parameter `end` (default is `\n`).

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
result = to_string(1, 2, 3)
```

__Output__
```plaintext
result = '1 2 3\n'
```

### Example 2

__Input__
```python
data = [7, 3, 1, "hello", (1, 2, 3)]
result = to_string(*data, sep=", ", end="!")
```

__Output__
```plaintext
result = '7, 3, 1, hello, (1, 2, 3)!'
```