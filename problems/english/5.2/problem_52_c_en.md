## [Class Point 5.0](../../../solutions/5.2/52_c.py)

Agree that using operators is much more convenient than regular methods. Let's recall the `move(x, y)` method we implemented and write an alternative using the `+` and `+=` operators.

When running the code `point + (x, y)`, a new point is created, which differs from the original by the given tuple distance along the $x$ and $y$ axes.\
When running the code `point += (x, y)`, the original point is moved.

Let's remind that we are currently modernizing only the `PatchedPoint` class.

### Note

Your solution should only contain classes and functions.\
The solution should not contain any initialization calls for the required classes.

### Example 1

__Input__
```python
point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)
```

__Output__
```plaintext
(0, 0)
(0, 0) (2, -3) False
```

### Example 2

__Input__
```python
first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
```

__Output__
```plaintext
(9, -4) (9, -4) True
```