## [Классная точка 3.0](../../../solutions/5.2/52_a.py)

Давайте расширим функционал класса, написанного вами в задаче «Классная точка 2.0».

Создайте класс `PatchedPoint` — наследника уже написанного вами `Point`.

Требуется реализовать следующие виды инициализации нового класса:

- параметров не передано — координаты точки равны 0;
- передан один параметр — кортеж с координатами точки;
- передано два параметра — координаты точки.

### Примечание

Ваше решение должно содержать только классы и функции.\
В решении не должно быть вызовов инициализации требуемых классов.

### Пример 1

__Ввод__
```python
point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
```

__Вывод__
```plaintext
0 0
2 -3
```

### Пример 2

__Ввод__
```python
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
```

__Вывод__
```plaintext
16.76
16.76
```