## [Uniformity is not a Flaw](../../../solutions/4.3/43_g.py)

In many tasks, input data needs to be controlled, particularly their types, despite dynamic typing.

Develop the `same_type` decorator, which checks a variable number of positional parameters. If different types are detected, it prints the message __Обнаружены различные типы данных__ ("Different data types detected") and interrupts the execution of the function.

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
```

__Output__
```plaintext
Обнаружены различные типы данных
Fail
Обнаружены различные типы данных
Fail
2
```

### Example 2

__Input__
```python
@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
```

__Output__
```plaintext
Hello, world!
Обнаружены различные типы данных
Fail
Обнаружены различные типы данных
Fail
```