## [Truth Table](../../../solutions/3.4/34_r.py)

All modern electronic computing devices are built on Boolean algebra, which operates with the truth and falsehood of statements. Any programming language contains logical operations (in _Python_ these are [and, or, not](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)).

Most often, to work with complex statements, the method called "Truth Table" is used.\
The essence of the method is simple — all possible values of input variables are considered, and the result is computed for them.

Develop a program that builds a truth table for the entered complex logical expression.

### Input format

A logical expression involving three variables ($a$, $b$, $c$) that is valid in _Python_.

### Output format:

Print the truth table for the given expression.

### Note (from Yandex)

To execute _Python_ code written in strings, there are two wonderful functions: [exec](https://docs.python.org/3/library/functions.html#exec) and [eval](https://docs.python.org/3/library/functions.html#eval).

### Note (from Me)

Using exec and eval is considered bad practice, so for solving this task it is better to [convert from infix notation to postfix notation](https://www.youtube.com/live/km0E_i8Dtso?si=tnpIrI4mPoAVW1RG&t=1581):

```python
# Infix notation
a not b c and or

# Postfix notation
not a or b and c
```

and evaluate the expression using a stack.

### Example 1

__Input__
```plaintext
not a or b and c
```

__Output__
```plaintext
a b c f
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
a and not b and c
```

__Output__
```plaintext
a b c f
0 0 0 0
0 0 1 0
0 1 0 0
0 1 1 0
1 0 0 0
1 0 1 1
1 1 0 0
1 1 1 0
```