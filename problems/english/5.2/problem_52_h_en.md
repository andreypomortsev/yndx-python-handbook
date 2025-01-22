## [Fractions v0.5](../../../solutions/5.2/52_h.py)

The next stage of development will be the implementation of comparison methods: >, <, >=, <=, ==, !=.

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
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
```

__Output__
```plaintext
False True False True False False
```

### Example 2

__Input__
```python
a = Fraction(1, 3)
b = Fraction(6, 2).reverse()
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)
```

__Output__
```plaintext
False False True True True True
```