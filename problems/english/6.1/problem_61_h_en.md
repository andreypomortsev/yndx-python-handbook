## [Numerical Snake 3.0](../../../solutions/6.1/61_h.py)

Once, you helped preschoolers with various snake patterns. Let's implement it using arrays.

Write a function `snake` that takes the width ($M$) and height ($N$) of the snake, as well as a named parameter `direction`.

The `direction` parameter can take the following values:

- `H` — horizontal snake, used by default;
- `V` — vertical snake.

The function should return a matrix representing the snake, with cells of type `int16`.

### Note

Your solution should only contain functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
print(snake(5, 3))
```

__Output__
```plaintext
[[ 1  2  3  4  5]
 [10  9  8  7  6]
 [11 12 13 14 15]]
```

### Example 2

__Input__
```python
print(snake(5, 3, direction='V'))
```

__Output__
```plaintext
[[ 1  6  7 12 13]
 [ 2  5  8 11 14]
 [ 3  4  9 10 15]]
```