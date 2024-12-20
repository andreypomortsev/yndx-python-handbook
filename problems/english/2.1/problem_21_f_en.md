## [Receipt](../../../solutions/2.1/21_f.py)

Calculating change is easy, but printing a nice receipt is not so simple.

### Input Format:

- Name of the product;  
- Price of the product per kilogram;  
- Weight of the product in kilograms;  
- Amount of money the customer has.

### Output Format:

```plaintext
Чек
<product_name> - <weight>кг - <price>руб/кг
Итого: <total_cost>руб
Внесено: <money_provided>руб
Сдача: <change>руб
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
Чек
черешня - 3кг - 2руб/кг
Итого: 6руб
Внесено: 10руб
Сдача: 4руб
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
Чек
манго - 43кг - 187руб/кг
Итого: 8041руб
Внесено: 8041руб
Сдача: 0руб
```