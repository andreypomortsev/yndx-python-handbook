## [Циклический генератор](../../../solutions/4.3/43_i.py)

Напишите генератор `cycle`, который принимает список и работает аналогично итератору [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle).

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример 1

**Ввод**
```python
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
```

**Вывод**
```plaintext
1 2 3 1 2
```

### Пример 2

**Ввод**
```python
print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))
```

**Вывод**
```plaintext
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3
```