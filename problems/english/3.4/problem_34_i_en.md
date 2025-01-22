## [Multiplication table 3.0](../../../solutions/3.4/34_i.py)

The local stationery factory ordered a program that generates multiplication tables.\
Let's help the manufacturer.

### Input format

A single natural number is given — the required size of the table.

### Output format:

The multiplication table of the specified size.

### Note

[itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product) is a great way to avoid nested loops.

### Example 1

__Input__
```plaintext
3
```

__Output__
```plaintext
1 2 3
2 4 6
3 6 9
```

### Example 2

__Input__
```plaintext
5
```

__Output__
```plaintext
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
```