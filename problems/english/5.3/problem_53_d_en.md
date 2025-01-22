## [Parameter Control](../../../solutions/5.3/53_d.py)

Write a function `only_positive_even_sum`, which accepts two parameters and returns their sum.

If one of the parameters is not an integer, raise a `TypeError` exception.\
If one of the parameters is not a positive even number, raise a `ValueError` exception.

### Note

Your solution should only contain functions.\
There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
print(only_positive_even_sum("3", 2.5))
```

__Output__
```plaintext
Exception TypeError raised
```

### Example 2

__Input__
```python
print(only_positive_even_sum(-5, 4))
```

__Output__
```plaintext
Exception ValueError raised
```