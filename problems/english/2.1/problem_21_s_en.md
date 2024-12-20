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

**Input**
```plaintext
черешня
2
3
10
```

**Output**
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

**Input**
```plaintext
манго
187
43
8041
```

**Output**
```plaintext
================Чек================
Товар:                        манго
Цена:              43кг * 187руб/кг
Итого:                      8041руб
Внесено:                    8041руб
Сдача:                         0руб
===================================
```