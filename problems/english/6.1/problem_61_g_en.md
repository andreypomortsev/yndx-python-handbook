## [Chess Preparation](../../../solutions/6.1/61_g.py)

Imagine you're writing a computer game "Chess". You need to model a chessboard, which is represented as a matrix. A black square is represented by zero, and a white square by one. When viewing the board from above, the top-left square is white.

Write a function `make_board` that takes the size of the chessboard and returns a matrix representing the given board.

Set the element type of the matrix to `int8`.

### Note

Your solution should only contain functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
print(make_board(4))
```

__Output__
```plaintext
[[1 0 1 0]
 [0 1 0 1]
 [1 0 1 0]
 [0 1 0 1]]
```

### Example 2

__Input__
```python
print(make_board(6))
```

__Output__
```plaintext
[[1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]]
```