## [Расстановка спортсменов](../../../solutions/3.4/34_m.py)

Расстановка спортсменов на старте — сложная задача. Однако при помощи итераторов она решается за пару строк. Напишите программу, которая выводит список возможных расстановок спортсменов на старте.

### Формат ввода

В первой строке задано натуральное число $N$ — количество спортсменов.\
В следующих $N$ строках записаны имена спортсменов.

### Формат вывода:

Отсортированный по алфавиту список расстановок.\
Имена в каждой строке выводить через запятую и пробел.

### Пример 1

__Ввод__
```plaintext
3
Аня
Боря
Вова
```

__Вывод__
```plaintext
Аня, Боря, Вова
Аня, Вова, Боря
Боря, Аня, Вова
Боря, Вова, Аня
Вова, Аня, Боря
Вова, Боря, Аня
```

### Пример 2

__Ввод__
```plaintext
4
Вова
Аня
Дима
Боря
```

__Вывод__
```plaintext
Аня, Боря, Вова, Дима
Аня, Боря, Дима, Вова
Аня, Вова, Боря, Дима
Аня, Вова, Дима, Боря
Аня, Дима, Боря, Вова
Аня, Дима, Вова, Боря
Боря, Аня, Вова, Дима
Боря, Аня, Дима, Вова
Боря, Вова, Аня, Дима
Боря, Вова, Дима, Аня
Боря, Дима, Аня, Вова
Боря, Дима, Вова, Аня
Вова, Аня, Боря, Дима
Вова, Аня, Дима, Боря
Вова, Боря, Аня, Дима
Вова, Боря, Дима, Аня
Вова, Дима, Аня, Боря
Вова, Дима, Боря, Аня
Дима, Аня, Боря, Вова
Дима, Аня, Вова, Боря
Дима, Боря, Аня, Вова
Дима, Боря, Вова, Аня
Дима, Вова, Аня, Боря
Дима, Вова, Боря, Аня
```