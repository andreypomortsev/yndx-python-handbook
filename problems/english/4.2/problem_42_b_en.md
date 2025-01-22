## [Matrix Generator](../../../solutions/4.2/42_b.py)

Write a function `make_matrix` that creates, fills, and returns a matrix of a specified size.

Function parameters:

- _size_ — a tuple (width, height) or a single number (for creating a square matrix);
- _value_ — the value of the list elements (default is 0).

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
result = make_matrix(3)
```

__Output__
```plaintext
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

### Example 2

__Input__
```python
result = make_matrix((4, 2), 1)
```

__Output__
```plaintext
result = [
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
```