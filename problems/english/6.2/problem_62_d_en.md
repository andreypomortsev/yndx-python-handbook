## [Promotion](../../../solutions/6.2/62_d.py)

The store, for which you wrote the function in the previous task, is running a promotion:

__If you buy more than two items, you get a 50% discount.__

_Important: The discount only applies to products purchased in quantities greater than two._

Write a function `discount`, which takes the receipt from the previous task and returns the updated one considering the promotion.

### Note

Do not remove the `cheque` function, as it will be needed for testing.

Your solution should only contain functions.\
The solution should not include calls to the required functions.

### Example

__Input__
```python
products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
```

__Output__
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