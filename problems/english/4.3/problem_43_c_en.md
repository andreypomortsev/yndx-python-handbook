## [Polynomial of N-th Degree](../../../solutions/4.3/43_c.py)

Write a function `make_equation` that, given the coefficients, constructs a string that describes a valid Python expression without using the exponentiation operator.

A second-degree polynomial with coefficients $a$, $b$, and $c$, for example, can be written as:

$((a)∗x+b)∗x+c$

### Note

Your solution should contain only functions.\
There should be no calls to the required functions, except for recursive calls.\
The trace of the recursive function calls in the answer is not considered and is shown for example purposes.

### Example 1

__Input__
```python
result = make_equation(3, 2, 1)
```

__Output__
```plaintext
# Calling make_equation(3, 2, 1)
# Calling make_equation(3, 2)
# Calling make_equation(3)
result = '((3) * x + 2) * x + 1'
```

### Example 2

__Input__
```python
result = make_equation(3, 1, 5, 3)
```

__Output__
```plaintext
# Calling make_equation(3, 1, 5, 3)
# Calling make_equation(3, 1, 5)
# Calling make_equation(3, 1)
# Calling make_equation(3)
result = '(((3) * x + 1) * x + 5) * x + 3'
```