## [Name Validation](../../../solutions/5.3/53_g.py)

When registering in various services, users enter a lot of information. Correctly filling out the fields is an important part of the program's operation, so forms are equipped with data validation systems.

Write a function `name_validation` that takes one positional argument — a last name or first name.

If the parameter is not a string, raise a `TypeError` exception.

Also, develop custom errors:

- `CyrillicError` — raised if the value consists of anything other than Cyrillic letters;
- `CapitalError` — raised if the value doesn't start with an uppercase letter, or if an uppercase letter is found not at the start of the value.

Error handling should occur in the order specified in the task.

If everything is successful, the function should return the parameter unchanged.

### Note

There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
print(name_validation("user"))
```

__Output__
```plaintext
Exception CyrillicError raised
```

### Example 2

__Input__
```python
print(name_validation("иванов"))
```

__Output__
```plaintext
Exception CapitalError raised
```