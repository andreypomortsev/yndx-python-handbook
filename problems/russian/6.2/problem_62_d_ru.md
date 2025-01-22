## [Акция](../../../solutions/6.2/62_d.py)

Магазин, для которого вы писали функцию в предыдущей задаче, проводит акцию:

__При покупке больше двух товаров — скидка 50%__

_мелкий шрифт: скидка распространяется только на товары купленные в количестве более двух штук_

Напишите функцию `discount`, принимающую чек из прошлой задачи и возвращающую новый с учётом акции.

### Примечание

Не удаляйте функцию `cheque`, она потребуется для тестирования.

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример

__Ввод__
```python
products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
```

__Вывод__
```plaintext
  product  price  number  cost
0   cream     72       1    72
1    milk     58       2   116
2    soda     99       3   297
  product  price  number   cost
0   cream     72       1   72.0
1    milk     58       2  116.0
2    soda     99       3  148.5
```