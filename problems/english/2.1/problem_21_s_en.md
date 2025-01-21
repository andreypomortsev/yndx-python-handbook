## [Receipt Decoration](../../../solutions/2.1/21_s.py)

Let's tidy up the receipt that was printed earlier. All lines should be 35 characters long.

### Input Format

- Name of the product;
- Price of the product;
- Weight of the product;
- Amount of money the customer has.

### Output Format:

```
================Чек================
Товар:                    <product>
Цена:   <number>kg * <number>руб/кг
Итого:                  <number>руб
Внесено:                <number>руб
Сдача:                  <number>руб
===================================
```

### Example 1

__Input__
```plaintext
черешня
2
3
10
```

__Output__
```plaintext
================Чек================
Товар:                      черешня
Цена:                 3кг * 2руб/кг
Итого:                         6руб
Внесено:                      10руб
Сдача:                         4руб
===================================
```

### Example 2

__Input__
```plaintext
манго
187
43
8041
```

__Output__
```plaintext
================Чек================
Товар:                        манго
Цена:              43кг * 187руб/кг
Итого:                      8041руб
Внесено:                    8041руб
Сдача:                         0руб
===================================
```