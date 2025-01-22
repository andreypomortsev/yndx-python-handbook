## [Class Point 2.0](../../../solutions/5.1/51_b.py)

Let's extend the functionality of the class from the previous task.

Implement the following methods:

- `move`, which moves the point by a specified distance along the axes $x$ and $y$;
- `length`, which calculates the distance to a given point, rounded to two decimal places.

### Note

Your solution should only contain classes and functions.\
The solution should not contain initialization calls of the required classes.

### Example 1

__Input__
```python
point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
```

__Output__
```plaintext
3 5
5 2
```

### Example 2

__Input__
```python
first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
```

__Output__
```plaintext
16.76
16.76
```