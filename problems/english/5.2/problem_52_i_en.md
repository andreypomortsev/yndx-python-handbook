## [Fractions v0.6](../../../solutions/5.2/52_i.py)

_It probably should have been thought about earlier..._

These words are often uttered during software development.

Does everyone realize that integers are also fractions?! Therefore, we need to change the initialization system so that it can handle integers as well (including as strings). And, naturally, we need to rewrite the arithmetic and comparison operators.

### Note

We will assume that the user is aware of the division-by-zero prohibition.\
All fields and methods that are not required for the task should be encapsulated (named using leading underscores).

Your solution should only contain classes and functions.\
There should be no initialization calls for the required classes in the solution.

### Example 1

__Input__
```python
a = Fraction(1)
b = Fraction('2')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
```

__Output__
```plaintext
1/1 2/1 1/3 1/1
False False
True True False True
```

### Example 2

__Input__
```python
a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
```

__Output__
```plaintext
1/2 2/3 2/5 -3/1
False True
False False False False
```