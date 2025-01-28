## [Merge with Validation](../../../solutions/5.3/53_e.py)

Once, you wrote a function `merge` that merges two sorted tuples.

Let's modify it a bit.

We'll introduce a system of checks:

- If one of the parameters is not an iterable object, raise a `StopIteration` exception;
- If the values of the input parameters contain "heterogeneous" data, raise a `TypeError` exception;
- If one of the parameters is not sorted, raise a `ValueError` exception.

The checks should be performed in the specified order.

If the parameters pass all checks, return an iterable object that is the merge of the two given parameters.

### Note

There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
print(*merge(35, (1, 2, 3)))
```

__Output__
```plaintext
Exception StopIteration raised
```

### Example 2

__Input__
```python
print(*merge([3, 2, 1], range(10)))
```

__Output__
```plaintext
Exception ValueError raised
```