## [Error Handling](../../../solutions/5.3/53_a.py)

Your solution will be provided with a function `func`, which has no parameters and no return value. However, during its execution, one of the following errors may occur: `ValueError`, `TypeError`, or `SystemError`.

Call the function, handle the error, and print its name. If no error occurs, print the message "No Exceptions".

### Example 1

__Input__
```python
def func():
    x = int('Hello, world!')
```

__Output__
```plaintext
ValueError
```

### Example 2

__Input__
```python
def func():
    x = '2' + 2
```

__Output__
```plaintext
TypeError
```