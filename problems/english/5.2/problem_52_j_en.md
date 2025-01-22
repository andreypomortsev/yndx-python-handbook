## [Fractions v0.7](../../../solutions/5.2/52_j.py)

_"Only the final touch left!"_ Doesn't that sound like mockery?

We "taught" our fractions to work with integers, and now we need to reverse the process. Implement functionality that will allow performing all arithmetic operations with fractions and numbers, regardless of their position (on the left or right) in the operator.

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
c, d = map(Fraction.reverse, (2 + a, -1 + b))
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
c, d = map(Fraction.reverse, (3 - a, 2 / b))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
```

__Output__
```plaintext
1/2 2/3 2/5 1/3
False True
False False False False
```