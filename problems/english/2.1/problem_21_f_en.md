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

__Input__  
```plaintext
черешня
2
3
10
```

__Output__  
```plaintext
Чек
черешня - 3кг - 2руб/кг
Итого: 6руб
Внесено: 10руб
Сдача: 4руб
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
Чек
манго - 43кг - 187руб/кг
Итого: 8041руб
Внесено: 8041руб
Сдача: 0руб
```