## [Breaking is not Building](../../../solutions/5.3/53_b.py)

Let's play a little "bug user".

Your solution will be provided with a function `func`, which takes two positional parameters and performs some __mathematical__ operation on them.

Propose a function call that will guaranteedly cause an error inside the function.

### Note

If the error occurs inside the function, it will be caught and handled.\
If the error occurs in your code, the program will terminate with an error.

### Example 1

__Input__
```python
def func(a, b):
    return a + b
```

__Output__
```plaintext
Ура! Ошибка!
```

### Example 2

__Input__
```python
def func(a, b):
    return a * b
```

__Output__
```plaintext
Ура! Ошибка!
```