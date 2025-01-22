## [Athlete lineup](../../../solutions/3.4/34_m.py)

Positioning athletes at the starting line is a tricky task. However, using iterators, it can be done in just a couple of lines. Write a program that outputs a list of possible athlete lineups.

### Input format

The first line contains a natural number $N$ — the number of athletes. The following $N$ lines contain the names of the athletes.

### Output format:

A sorted list of lineups. Names in each line should be printed separated by commas and spaces.

### Example 1

__Input__
```plaintext
3
Аня
Боря
Вова
```

__Output__
```plaintext
Аня, Боря, Вова
Аня, Вова, Боря
Боря, Аня, Вова
Боря, Вова, Аня
Вова, Аня, Боря
Вова, Боря, Аня
```

### Example 2

__Input__
```plaintext
4
Вова
Аня
Дима
Боря
```

__Output__
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