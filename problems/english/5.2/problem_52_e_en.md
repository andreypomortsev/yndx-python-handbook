## [Fractions v0.2](../../../solutions/5.2/52_e.py)

Let's continue developing the `Fraction` class, which implements the proposed fractions.

Provide the ability to set a negative numerator and/or denominator. Also, rewrite the methods `__str__` and `__repr__` to ensure the object information aligns with initialization via string.

Next, implement the mathematical negation operator — the unary minus.

### Note

Let's assume that the user knows about the prohibition of division by zero.\
All fields and methods not required for the task should be encapsulated (named with leading underscores).

Your solution should only contain classes and functions.\
The solution should not contain any initialization calls for the required classes.

### Example 1

__Input__
```python
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
```

__Output__
```plaintext
1/3 1/3 -1/3 -1/3
Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')
```

### Example 2

__Input__
```python
a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
```

__Output__
```plaintext
-1/2 1/2 False
1/3 -1/2
1 3
1 2
```