## [Fractions v0.4](../../../solutions/5.2/52_g.py)

Let's continue developing the `Fraction` class, which implements the proposed fractions.

Implement the binary operators:

- `*` — multiplication of fractions, creates a new fraction;
- `/` — division of fractions, creates a new fraction;
- `*=` — multiplication of fractions, modifies the fraction on the left;
- `/=` — division of fractions, modifies the fraction on the left.

Also, develop the `reverse` method, which returns the reciprocal fraction.

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
c = a * b
print(a, b, c, a is c, b is c)
```

__Output__
```plaintext
1/3 1/2 1/6 False False
```

### Example 2

__Input__
```python
a = Fraction(1, 3)
c = b = Fraction(2, 1).reverse()
b /= a
print(a, b, c, b is c)
```

__Output__
```plaintext
1/3 3/2 3/2 True
```