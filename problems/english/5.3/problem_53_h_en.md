## [Username Validation](../../../solutions/5.3/53_h.py)

We will continue to implement the validation system.

Write a function `username_validation` that takes one positional argument — a username:

If the parameter is not a string, raise a `TypeError` exception.

Also, develop custom errors:

- `BadCharacterError` — raised if the value contains anything other than Latin letters, digits, and the underscore symbol;
- `StartsWithDigitError` — raised if the value starts with a digit.

Error handling should occur in the order specified in the task.

If everything is successful, the function should return the parameter unchanged.

### Note

There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
print(username_validation("$user_45$"))
```

__Output__
```plaintext
Exception BadCharacterError raised
```

### Example 2

__Input__
```python
print(username_validation("45_user"))
```

__Output__
```plaintext
Exception StartsWithDigitError raised
```