## [Кашееды](../../../solutions/3.2/32_d.py)

Каждый воспитанник детского сада любит либо манную, либо овсяную, либо обе каши.\
Давайте создадим программу, которая позволит воспитателю быстро выяснить, сколько детей любят обе каши.

### Формат ввода

В первых двух строках указывается количество детей, любящих манную и овсяную каши ($N$ и $M$).\
Затем идут $N$ строк — фамилии детей, которые любят манную кашу, и $M$ строк с фамилиями детей, любящих овсяную кашу.\
Гарантируется, что в группе нет однофамильцев.

### Формат вывода:

Количество учеников, которые любят обе каши.\
Если таких не окажется, в строке вывода нужно написать «Таких нет».

### Пример 1

__Ввод__
```plaintext
3
2
Васильев
Петров
Васечкин
Иванов
Михайлов
```

__Вывод__
```plaintext
Таких нет
```

### Пример 2

__Ввод__
```plaintext
3
3
Иванов
Петров
Васечкин
Иванов
Петров
Васечкин
```

__Вывод__
```plaintext
3
```