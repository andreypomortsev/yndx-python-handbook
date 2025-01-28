## [Class Rectangle 3.0](../../../solutions/5.1/51_g.py)

You need to improve the previous task a little more.

Develop the following methods:

- `turn()` — rotates the rectangle 90° clockwise around its center;
- `scale(factor)` — changes the size by the specified factor, also relative to the center.

All calculations should be rounded to two decimal places.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
```

__Output__
```plaintext
(-3.14, 2.71)
(6.28, 5.42)
(-2.71, 3.14)
(5.42, 6.28)
```

### Example 2

__Input__
```python
rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
```

__Output__
```plaintext
(-3.14, 2.71)
(6.28, 5.42)
(-6.28, 5.42)
(12.56, 10.84)
```