## [Генератор списков](../../../solutions/4.2/42_a.py)

Большинство задач этой главы ориентировано на отработку навыков по разработке функций.

Ваше решение будет использоваться как библиотека.

Напишите функцию `make_list`, которая создаёт, заполняет и возвращает список заданного размера.

Параметры функции:

- _length_ — требуемая длина списка;
- _value_ — значение элементов списка (по-умолчанию 0).

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример 1

__Ввод__
```python
result = make_list(3)
```

__Вывод__
```plaintext
result = [0, 0, 0]
```

### Пример 2

__Ввод__
```python
result = make_list(5, 1)
```

__Вывод__
```plaintext
result = [1, 1, 1, 1, 1]
```