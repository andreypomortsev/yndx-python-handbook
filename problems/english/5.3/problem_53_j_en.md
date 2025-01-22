## [Password Validation](../../../solutions/5.3/53_j.py)

After the user has entered their data in the required format, you can take care of the password as well.

Write a function `password_validation` that accepts one positional parameter — the password, and the following named parameters:

- `min_length` — the minimum length of the password, default is 8;
- `possible_chars` — a string of characters that may be in the password, default is Latin letters and digits;
- `at_least_one` — a function returning a boolean value, default is `str.isdigit`.
If the provided positional parameter is not a string, raise a `TypeError` exception.

Also, implement custom exceptions:

- `MinLengthError` — raised if the password is shorter than the required length;
- `PossibleCharError` — raised if the password contains an invalid character;
- `NeedCharError` — raised if the password does not contain any required characters.

The checks should be performed in the order specified in the task.

Since a good developer never stores passwords in plain text, the function, upon successful completion, returns the hash of the password. For this, use the `_sha256_` function from the [hashlib](https://docs.python.org/3/library/hashlib.html) package and return its hexadecimal representation.

### Note

The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
print(password_validation("Hello12345"))
```

__Output__
```plaintext
67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1
```

### Example 2

__Input__
```python
print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
```

__Output__
```plaintext
PossibleCharError exception raised
```