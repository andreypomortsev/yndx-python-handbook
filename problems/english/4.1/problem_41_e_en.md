## [Numerical String](../../../solutions/4.1/41_e.py)

Develop a function `split_numbers` that takes a string of integers separated by spaces and returns a tuple of these numbers.

### Note

Your solution should contain only functions.\
The solution should not contain calls to the required functions.

You may ask: why a tuple and not a list? It's all about safety. Tuples are immutable collections and it's safer to pass them to or from a function.

### Example 1

__Input__
```python
result = split_numbers("1 2 3 4 5")
```

__Output__
```plaintext
result = (1, 2, 3, 4, 5)
```

### Example 2

__Input__
```python
result = split_numbers("1 -2 3 -4 5")
```

__Output__
```plaintext
result = (1, -2, 3, -4, 5)
```