## [Cool Rectangle](../../../solutions/5.1/51_e.py)

Let's move on to more complex geometric shapes.

Develop the `Rectangle` class.

When initialized, the class accepts two tuples of rational coordinates of opposite corners of the rectangle (with sides parallel to the coordinate axes).

The class should implement the following methods:

- `perimeter` — returns the perimeter of the rectangle;
- `area` — returns the area of the rectangle.

All calculation results should be rounded to two decimal places.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
```

__Output__
```plaintext
23.52
```

### Example 2

__Input__
```python
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
```

__Output__
```plaintext
32.14
```