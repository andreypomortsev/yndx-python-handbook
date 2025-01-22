## [Breaking is not Building 2](../../../solutions/5.3/53_c.py)

Your solution will be provided with a function `func`, which this time accepts an unlimited number of positional parameters and performs some __type casting__ operation on them.

Propose a function call that will guaranteedly cause an error inside the function.

### Note

If the error occurs inside the function, it will be caught and handled.\
If the error occurs in your code, the program will terminate with an error.

### Example 1

__Input__
```python
def func(a, b, c):
    return ''.join(map(str, (a, b, c)))
```

__Output__
```plaintext
Ура! Ошибка!
```

### Example 2

__Input__
```python
def func(a, b):
    return set(a) ^ set(b)
```

__Output__
```plaintext
Ура! Ошибка!
```