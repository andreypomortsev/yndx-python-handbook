## [Menu 2.0](../../../solutions/3.4/34_h.py)

In the kindergarten, a new porridge is served for breakfast every day.

Write a program that creates a schedule of porridges for the upcoming days.

### Input format

A natural number $M$ is given — the number of porridges on the menu. Each of the following $M$ lines contains one porridge name. At the end, a natural number $N$ is given — the number of days.

### Output format:

Print the list of porridges in the order they will be served.

### Note

It is recommended to study the documentation for the function [`itertools.islice`](https://docs.python.org/3/library/itertools.html#itertools.islice), which implements slices based on iterators.

### Example 1

__Input__
```plaintext
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
3
```

__Output__
```plaintext
Манная
Гречневая
Пшённая
```

### Example 2

__Input__
```plaintext
5
Манная
Гречневая
Пшённая
Овсяная
Рисовая
12
```

__Output__
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