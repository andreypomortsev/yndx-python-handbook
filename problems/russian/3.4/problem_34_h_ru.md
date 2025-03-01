## [Меню питания 2.0](../../../solutions/3.4/34_h.py)

В детском саду ежедневно подают новую кашу на завтрак.

Напишите программу, которая строит расписание каш на ближайшие дни.

### Формат ввода

Вводится натуральное число $M$ — количество каш в меню. В каждой из последующих $M$ строк записано одно название каши. В конце передается натуральное число $N$ — количество дней.

### Формат вывода:

Вывести список каш в порядке подачи.

### Примечание

Советуем изучить документацию на функцию [`itertools.islice`](https://docs.python.org/3/library/itertools.html#itertools.islice), которая реализует срезы на основе итераторов.

### Пример 1

__Ввод__
```plaintext
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
3
```

__Вывод__
```plaintext
Манная
Гречневая
Пшённая
```

### Пример 2

__Ввод__
```plaintext
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
12
```

__Вывод__
```plaintext
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая
Пшённая
Овсяная
Рисовая
Манная
Гречневая
```