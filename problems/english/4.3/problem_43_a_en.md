## [Recursive Summator](../../../solutions/4.3/43_a.py)

Most of the tasks in this chapter focus on developing recursive function skills.

Your solution will be used as a library.

Write a function `recursive_sum` that finds the sum of all positional arguments.

### Note

Your solution should contain only functions.\
There should be no calls to the required functions, except for recursive calls.\
The trace of the recursive function calls in the answer is not considered and is shown for example purposes.

### Example 1

__Input__
```python
result = recursive_sum(1, 2, 3)
```

__Output__
```plaintext
# Calling recursive_sum(1, 2, 3)
# Calling recursive_sum(1, 2)
# Calling recursive_sum(1)
# Calling recursive_sum()
result = 6
```

### Example 2

__Input__
```python
result = recursive_sum(7, 1, 3, 2, 10)
```

__Output__
```plaintext
# Calling recursive_sum(7, 1, 3, 2, 10)
# Calling recursive_sum(7, 1, 3, 2)
# Calling recursive_sum(7, 1, 3)
# Calling recursive_sum(7, 1)
# Calling recursive_sum(7)
# Calling recursive_sum()
result = 23
```
