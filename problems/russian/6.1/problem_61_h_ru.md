## [Числовая змейка 3.0](../../../solutions/6.1/61_h.py)

Когда-то вы помогали детсадовцам с различными змейками. Давайте реализуем её на основе массивов.

Напишите функцию snake, которая принимает ширину ($M$) и высоту ($N$) змейки, а также именованный параметр `direction`.

Параметр `direction` могут принимать значения:

- `H` — горизонтальная змейка, используется по умолчанию;
- `V` — вертикальная змейка.

Функция должна вернуть матрицу, представляющую змейку, с ячейками типа `int16`.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример 1

__Ввод__
```python
print(snake(5, 3))
```

__Вывод__
```plaintext
[[ 1  2  3  4  5]
 [10  9  8  7  6]
 [11 12 13 14 15]]
```

### Пример 2

__Ввод__
```python
print(snake(5, 3, direction='V'))
```

__Вывод__
```plaintext
[[ 1  6  7 12 13]
 [ 2  5  8 11 14]
 [ 3  4  9 10 15]]
```