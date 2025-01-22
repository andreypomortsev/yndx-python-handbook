## [Result Decorator](../../../solutions/4.3/43_d.py)

Write a decorator `answer` that transforms a function, which accepts an unlimited number of positional and keyword arguments, and returns its result with the prefix "Result of the function: <value>".

### Note

Your solution should contain only functions.\
There should be no calls to the required functions.

### Example 1

__Input__
```python
@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))
```

__Output__
```plaintext
Результат функции: 8
Результат функции: 16
```

### Example 2

__Input__
```python
@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
```

__Output__
```plaintext
Результат функции: dehlorw
Результат функции: адекортуыэ
```