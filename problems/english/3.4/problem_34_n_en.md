## [Sports Predictions](../../../solutions/3.4/34_n.py)

It's great that the athletes are lined up at the start, but predicting the finalists is nearly impossible. Let's write a program that outputs a list of possible winners.

### Input format

The first line contains a natural number $N$ — the number of athletes. The following $N$ lines contain the names of the athletes.

### Output format:

A sorted list of all possible outcomes. Names in each line should be printed separated by commas and spaces.

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
Аня, Боря, Вова
Аня, Боря, Дима
Аня, Вова, Боря
Аня, Вова, Дима
Аня, Дима, Боря
Аня, Дима, Вова
Боря, Аня, Вова
Боря, Аня, Дима
Боря, Вова, Аня
Боря, Вова, Дима
Боря, Дима, Аня
Боря, Дима, Вова
Вова, Аня, Боря
Вова, Аня, Дима
Вова, Боря, Аня
Вова, Боря, Дима
Вова, Дима, Аня
Вова, Дима, Боря
Дима, Аня, Боря
Дима, Аня, Вова
Дима, Боря, Аня
Дима, Боря, Вова
Дима, Вова, Аня
Дима, Вова, Боря
```