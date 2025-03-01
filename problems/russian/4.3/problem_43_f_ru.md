## [Сортировка слиянием](../../../solutions/4.3/43_f.py)

Мы уже реализовывали функцию `merge`, которая способна "слить" два отсортированных списка в один.\
Чаще всего её применяют в рекурсивном алгоритме сортировки слиянием.

Напишите рекурсивную функцию `merge_sort`, которая производит сортировку списка.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций, за исключением рекурсивных.\
Трассировка вызова рекурсивной функции в обработке ответа не учитывается и показана для примера.

### Пример 1

__Ввод__
```python
result = merge_sort([3, 2, 1])
```

__Вывод__
```plaintext
# Вызов merge_sort([3, 2, 1])
# Вызов merge_sort([3])
# Вызов merge_sort([2, 1])
# Вызов merge_sort([2])
# Вызов merge_sort([1])
result = [1, 2, 3]
```

### Пример 2

__Ввод__
```python
result = merge_sort([3, 1, 5, 3])
```

__Вывод__
```plaintext
# Вызов merge_sort([3, 1, 5, 3])
# Вызов merge_sort([3, 1])
# Вызов merge_sort([3])
# Вызов merge_sort([1])
# Вызов merge_sort([5, 3])
# Вызов merge_sort([5])
# Вызов merge_sort([3])
result = [1, 3, 3, 5]
```