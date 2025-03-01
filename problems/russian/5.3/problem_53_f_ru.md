## [Корень зла 2](../../../solutions/5.3/53_f.py)

В одной из первых лекций вы уже решали задачу о поиске корней уравнения. Давайте модернизируем её.

Напишите функцию `find_roots`, принимающую три параметра: коэффициенты уравнения и возвращающую его корни в виде кортежа из двух значений.

Так же создайте два собственных исключения `NoSolutionsError` и `InfiniteSolutionsError`, которые будут вызваны в случае отсутствия и бесконечного количества решений уравнения соответственно.

Если переданные коэффициенты не являются рациональными числами, вызовите исключение `TypeError`.

### Примечание

В решении не должно быть вызовов требуемых функций.

### Пример 1

__Ввод__
```python
print(find_roots(0, 0, 1))
```

__Вывод__
```plaintext
Вызвано исключение NoSolutionsError
```

### Пример 2

__Ввод__
```python
print(find_roots(1, 2, 1))
```

__Вывод__
```plaintext
(-1.0, -1.0)
```