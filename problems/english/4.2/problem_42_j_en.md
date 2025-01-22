## [Key Secret](../../../solutions/4.2/42_j.py)

Vasya loves secrets and encryption. He often uses a substitution cipher and asks you to develop a function that will allow him to quickly encrypt messages.

Write a function `secret_replace(text, **replaces)` that accepts:

- the text that needs to be encrypted;
- named arguments — substitution rules, which are tuples of one or more values.

The function should return the encrypted text.

### Note

Your solution should contain only functions.\
There should be no calls to the required functions in the solution.

Note that the positional argument in the required function should not have a single-letter name. To understand the error, examine the following code:

```python
def func(a, **b):
    ...

func(1, **{'a': 2})
```

### Example 1

__Input__
```python
result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
```

__Output__
```python
result = 'Hehiy123, wzrhid!'
```

### Example 2

__Input__
```python
result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
```

__Output__
```python
result = 'Z3X1-G!0Z371'
```