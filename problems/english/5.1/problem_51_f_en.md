## [Class Rectangle 2.0](../../../solutions/5.1/51_f.py)

Let's expand the functionality of the class you wrote in the previous task.

Implement the following methods:

- `get_pos()` — returns the coordinates of the top-left corner as a tuple;
- `get_size()` — returns the dimensions as a tuple;
- `move(dx, dy)` — changes the position by the specified values;
- `resize(width, height)` — changes the size (the position of the top-left corner remains unchanged).

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
```

__Output__
```plaintext
(3.2, 3.14) (4.32, 7.44)
(4.52, -1.86) (4.32, 7.44)
```

### Example 2

__Input__
```python
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
```

__Output__
```plaintext
(3.2, 3.14) (4.32, 7.44)
(3.2, 3.14) (23.5, 11.3)
```