## ["Straightening" a List](../../../solutions/4.3/43_j.py)

Often, the data we receive from various sources doesn't meet our needs. One common issue is excessive nesting of lists.

Write the function `make_linear`, which takes a list of lists and returns its "flattened" representation.

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions, except for recursive ones.\
The trace of the recursive function call in the response is not considered and is shown for illustration purposes.

### Example 1

__Input__
```python
result = make_linear([1, 2, [3]])
```

__Output__
```plaintext
# Call make_linear([1, 2, [3]])
# Call make_linear([3])
result = [1, 2, 3]
```

### Example 2

__Input__
```python
result = make_linear([1, [2, [3, 4]], 5, 6])
```

__Output__
```plaintext
# Call make_linear([1, [2, [3, 4]], 5, 6])
# Call make_linear([2, [3, 4]])
# Call make_linear([3, 4])
result = [1, 2, 3, 4, 5, 6]
```