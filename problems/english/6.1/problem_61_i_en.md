## [Rotation](../../../solutions/6.1/61_i.py)

Write a function `rotate` that takes a two-dimensional matrix and one of the rotation angles: $90^\circ$, $180^\circ$, $270^\circ$, and $360^\circ$.

The function should return a new matrix corresponding to the given clockwise rotation.

### Note

Your solution should only contain functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
print(rotate(np.arange(12).reshape(3, 4), 90))
```

__Output__
```plaintext
[[ 8  4  0]
 [ 9  5  1]
 [10  6  2]
 [11  7  3]]
```

### Example 2

__Input__
```python
print(rotate(np.arange(12).reshape(3, 4), 270))
```

__Output__
```plaintext
[[ 3  7 11]
 [ 2  6 10]
 [ 1  5  9]
 [ 0  4  8]]
```