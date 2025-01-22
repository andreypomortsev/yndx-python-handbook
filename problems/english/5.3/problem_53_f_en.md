## [Root of Evil 2](../../../solutions/5.3/53_f.py)

In one of the earlier lectures, you solved the problem of finding the roots of an equation. Let's modernize it.

Write a function `find_roots` that takes three parameters: the coefficients of the equation and returns its roots as a tuple of two values.

Also, create two custom exceptions `NoSolutionsError` and `InfiniteSolutionsError`, which will be raised in case of no solutions and infinite solutions, respectively.

If the provided coefficients are not rational numbers, raise a `TypeError` exception.

### Note

There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
print(find_roots(0, 0, 1))
```

__Output__
```plaintext
Exception NoSolutionsError raised
```

### Example 2

__Input__
```python
print(find_roots(1, 2, 1))
```

__Output__
```plaintext
(-1.0, -1.0)
```