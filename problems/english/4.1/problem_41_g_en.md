## [Chess "Lunch"](../../../solutions/4.1/41_g.py)

Write a function `can_eat` that takes the positions of a knight and another piece as tuples of two coordinates, and returns a boolean value: `True` if the knight can capture the piece, and `False` otherwise.

### Note

Your solution should contain only functions.\
The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
result = can_eat((2, 1), (4, 2))
```

__Output__
```plaintext
result = True
```

### Example 2

__Input__
```python
result = can_eat((5, 5), (6, 6))
```

__Output__
```plaintext
result = False
```