## [Shopping List 2.0](../../../solutions/3.4/34_l.py)

Let's help the person with shopping again. Write a program that combines the family's wishes into one list.

### Input format

The first line contains a natural number $N$ — the number of family members. The next $N$ lines contain the desired products (separated by commas and spaces).

### Output format:

A sorted list of products in alphabetical order with numbering.

### Note

Remember that iterators can be stored in a list, and the list can be unpacked into any function.

### Example 1

__Input__
```plaintext
3
картина, корзина, картонка
мыло, манка
молоко, хлеб, сыр
```

__Output__
```plaintext
1. картина
2. картонка
3. корзина
4. манка
5. молоко
6. мыло
7. сыр
8. хлеб
```

### Example 2

__Input__
```plaintext
2
печенье, сушки
чай, кофе
```

__Output__
```plaintext
1. кофе
2. печенье
3. сушки
4. чай
```