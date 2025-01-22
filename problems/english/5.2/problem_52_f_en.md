## [Fractions v0.3](../../../solutions/5.2/52_f.py)

Let's continue developing the `Fraction` class, which implements the proposed fractions.

Implement the binary operators:

- `+` — addition of fractions, creates a new fraction;
- `-` — subtraction of fractions, creates a new fraction;
- `+=` — addition of fractions, modifies the fraction on the left;
- `-=` — subtraction of fractions, modifies the fraction on the left.

### Note

Let's assume that the user knows about the prohibition of division by zero.\
All fields and methods not required for the task should be encapsulated (named with leading underscores).

Your solution should only contain classes and functions.\
The solution should not contain any initialization calls for the required classes.

### Example 1

__Input__
```python
a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)
```

__Output__
```plaintext
1/3 1/2 5/6 False False
```

### Example 2

__Input__
```python
a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
```

__Output__
```plaintext
1/8 1/4 1/4 True
```