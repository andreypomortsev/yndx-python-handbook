## [Чек - 2](../../../solutions/6.2/62_c.py)

В местном магазине решили добавить анализ данных и каждый чек представлять в виде _DataFrame_.
Прайс-лист уже сформирован в виде объекта _Series_, где индексами являются названия, а значениями — цены.

Напишите функцию, cheque, которая принимает прайс-лист и список покупок в виде неопределённого количества именованных параметров (ключ — название товара, значение — количество).

Функция должна вернуть объект _DataFrame_ со столбцами:

- наименование продукта (product);
- цена за единицу (price);
- количество (number);
- итоговая цена (cost).

Строки чека должны быть отсортированы по названию продуктов в лексикографическом порядке.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример

__Ввод__
```python
products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
```

__Вывод__
```plaintext
  product  price  number  cost
0   cream     72       1    72
1    milk     58       2   116
2    soda     99       3   297
```

## Подход к решению

__Создание базового DataFrame__

   - На основе объекта _Series_, представляющего прайс-лист, создаётся _DataFrame_ с двумя колонками: 
        - `product` (наименование товара)
        - `price` (цена за единицу).

__Добавление количества товаров__

   - Количество товаров передаётся через именованные параметры `**products` и преобразуется в объект _Series_, где ключами являются названия товаров, а значениями — количество.
   - С помощью метода `merge` этот объект объединяется с ранее созданным _DataFrame_. При этом товары сопоставляются по колонке `product`.

__Сортировка по названию товаров__

   - После объединения данных выполняется сортировка строк _DataFrame_ по колонке `product` в лексикографическом порядке с помощью метода `sort_values`.

__Вычисление итоговой стоимости__

   - Итоговая стоимость для каждого товара вычисляется через выражение `price * number`. Новая колонка `cost` добавляется в _DataFrame_ с использованием метода `assign`.

__Сброс индексов__

   - Для удобства вывода и чтения результирующий _DataFrame_ приводится к стандартному виду с последовательными индексами через `reset_index(drop=True)`.
