## [Class Point 4.0](../../../solutions/5.2/52_b.py)

Now, let's further enhance the `PatchedPoint` class. Implement the magic methods `__str__` and `__repr__`.

When converting to a string, the point should be represented in the format $(x, y)$.
The `__repr__` method should return a string for initializing the point with two parameters.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
```

__Output__
```plaintext
(0, 0)
PatchedPoint(2, -3)
```

### Example 2

__Input__
```python
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
```

__Output__
```plaintext
(2, -7) (7, 9)
PatchedPoint(2, -7) PatchedPoint(7, 9)
```