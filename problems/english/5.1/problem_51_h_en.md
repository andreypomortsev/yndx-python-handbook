## [Checkers](../../../solutions/5.1/51_h.py)

Checkers is a very engaging game that is relatively easy to model.

The rules involve two classes: a game board and a checker. However, we will simplify the task and instead of a checker, we will manipulate cells that can have three states: empty, white checker, and black checker.

Develop two classes: `Checkers` and `Cell`.

Objects of the `Checkers` class, when initialized, build a game board with a standard distribution of cells and should have the following methods:

- `move(f, t)` — moves a checker from position `f` to position `t`;
- `get_cell(p)` — returns the "cell" object at position `p`.

Objects of the `Cell` class, when initialized, take one of three states:
- __W__ — white checker,
- __B__ — black checker,
- __X__ — empty cell,

and also have the method `status()` that returns the state set in it.

The coordinates of the cells are described by strings in the form of PQ, where:

- P — the column of the game board, one of the uppercase Latin letters: ABCDEFGH;
- Q — the row of the game board, one of the digits: 12345678.

We will assume that the user always moves correctly, and there is no need to check for move validity.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
```

__Output__
```plaintext
XBXBXBXB
BXBXBXBX
XBXBXBXB
XXXXXXXX
XXXXXXXX
WXWXWXWX
XWXWXWXW
WXWXWXWX
```

### Example 2

__Input__
```python
checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()
```

__Output__
```plaintext
XBXBXBXB
BXBXBXBX
XBXBXBXX
XXXXXXBX
XXXWXXXX
WXXXWXWX
XWXWXWXW
WXWXWXWX
```