## [Cyclic Generator](../../../solutions/4.3/43_i.py)

Write a `cycle` generator that takes a list and behaves similarly to the iterator [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle).

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
```

__Output__
```plaintext
1 2 3 1 2
```

### Example 2

__Input__
```python
print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
```

__Output__
```plaintext
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3
```