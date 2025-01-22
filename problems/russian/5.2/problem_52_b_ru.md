## [Классная точка 4.0](../../../solutions/5.2/52_b.py)

А теперь модернизируем уже новый класс `PatchedPoint`. Реализуйте магические методы `__str__` и `__repr__`.

При преобразовании в строку точка представляется в формате $(x, y)$.\
Репрезентация же должна возвращать строку для инициализации точки двумя параметрами.

### Примечание

Ваше решение должно содержать только классы и функции.\
В решении не должно быть вызовов инициализации требуемых классов.

### Пример 1

__Ввод__
```python
point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))
```

__Вывод__
```plaintext
(0, 0)
PatchedPoint(2, -3)
```

### Пример 2

__Ввод__
```python
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
```

__Вывод__
```plaintext
(2, -7) (7, 9)
PatchedPoint(2, -7) PatchedPoint(7, 9)
```