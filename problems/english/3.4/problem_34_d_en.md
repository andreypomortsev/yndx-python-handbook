## [Dictionary Tree](../../../solutions/3.4/34_d.py)

Write a program that transforms a string of words into a tree shape as shown in the example.

### Input Format

A single line of words separated by spaces is provided.

### Output Format:

Multiple lines, each containing one more word than the previous one.

### Note

The [accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate) function "adds" not only numbers.

### Example 1

__Input__
```plaintext
мама мыла раму
```

__Output__
```plaintext
мама
мама мыла
мама мыла раму
```

### Example 2

__Input__
```plaintext
картина корзина картонка
```

__Output__
```plaintext
картина
картина корзина
картина корзина картонка
```