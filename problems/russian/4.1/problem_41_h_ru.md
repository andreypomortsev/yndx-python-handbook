## [А роза упала на лапу Азора 7.0](../../../solutions/4.1/41_h.py)

Напишите функцию `is_palindrome`, которая принимает натуральное число, строку, кортеж или список, а возвращает логическое значение: `True` — если передан палиндром, а в противном случае — `False`.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

Для определения типа параметра можно воспользоваться функцией [type](https://docs.python.org/3/library/functions.html#type) или более продвинутой [isinstance](https://docs.python.org/3/library/functions.html#isinstance).

### Пример 1

**Ввод**
```plaintext
result = is_palindrome(123)
```

**Вывод**
```plaintext
result = False
```

### Пример 2

**Ввод**
```plaintext
result = is_palindrome([1, 2, 1, 2, 1])
```

**Вывод**
```plaintext
result = True
```