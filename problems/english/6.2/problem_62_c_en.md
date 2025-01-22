## [Receipt - 2](../../../solutions/6.2/62_c.py)

The local store decided to add data analysis and represent each receipt as a _DataFrame_.
The price list has already been created as a _Series_ object, where the indices are the product names, and the values are the prices.

Write a function, `cheque`, that takes the price list and a list of purchases as an indefinite number of named parameters (key — product name, value — quantity).

The function should return a _DataFrame_ object with the following columns:

- product name (product);
- price per unit (price);
- quantity (number);
- total price (cost).

The rows of the receipt should be sorted lexicographically by product name.

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example

__Input__
```python
products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
```

__Output__
```plaintext
  product  price  number  cost
0   cream     72       1    72
1    milk     58       2   116
2    soda     99       3   297
```

## Approach

__Creating the base DataFrame__

   - A _DataFrame_ is created from the _Series_ object representing the price list, with two columns:
        - `product` (product name)
        - `price` (price per unit).

__Adding the quantity of products__

   - The quantity of products is passed through named parameters `**products` and is converted into a _Series_ object, where the keys are product names and the values are quantities.
   - This object is merged with the previously created _DataFrame_ using the `merge` method, where products are matched by the `product` column.

__Sorting by product name__

   - After merging the data, the rows of the _DataFrame_ are sorted by the `product` column in lexicographical order using the `sort_values` method.

__Calculating the total cost__

   - The total cost for each product is calculated using the expression `price * number`. A new `cost` column is added to the _DataFrame_ using the `assign` method.

__Resetting the indices__

   - For convenience and readability, the resulting _DataFrame_ is reset to a standard form with sequential indices using `reset_index(drop=True)`.