## [Truth Table 2](../../../solutions/3.4/34_s.py)

Let's continue working with truth tables. Think of a program that builds the truth table for a given complex logical expression.

### Input format

A logical expression involving multiple variables valid in Python.

### Output format:

Print the truth table for the given expression.

### Note (from Yandex)

In the expression, all variables are specified by uppercase Latin letters.\
Pay attention to the parameters `__globals` and `__locals` in the [eval](https://docs.python.org/3/library/functions.html#eval) function.

### Note (from Me)

Using exec and eval is considered bad practice, so for solving this task it is better to [convert from infix notation to postfix notation](https://www.youtube.com/live/km0E_i8Dtso?si=tnpIrI4mPoAVW1RG&t=1581):

```python
# Infix notation
not A or B and C

# Postfix notation
A not B C and or
```

and evaluate the expression using a stack.

### Example 1

__Input__
```plaintext
not A or B and C
```

__Output__
```plaintext
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 0
1 0 1 0
1 1 0 0
1 1 1 1
```

### Example 2

__Input__
```plaintext
A and not B and A
```

__Output__
```plaintext
A B F
0 0 0
0 1 0
1 0 1
1 1 0
```