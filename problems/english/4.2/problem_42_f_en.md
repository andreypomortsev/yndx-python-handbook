## [Coffee Shop](../../../solutions/4.2/42_f.py)

The management of a local programmer-themed coffee shop named _Java-0x00_ has decided to upgrade its coffee ordering system.

To achieve this, they need to implement a function `order`, which takes a list of customer preferences in descending order of desirability.

Each drink in the coffee shop is strictly defined by a recipe:

- __Эспрессо__ (Espresso) is made from: 1 unit of coffee beans.
- __Капучино__ (Cappuccino) is made from: 1 unit of coffee beans and 3 units of milk.
- __Макиато__ (Macchiato) is made from: 2 units of coffee beans and 1 unit of milk.
- __Кофе по-венски__ (Viennese Coffee) is made from: 1 unit of coffee beans and 2 units of whipped cream.
- __Латте Макиато__ (Latte Macchiato) is made from: 1 unit of coffee beans, 2 units of milk, and 1 unit of whipped cream.
- __Кон Панна__ (Con Panna) is made from: 1 unit of coffee beans and 1 unit of whipped cream.

A global variable `in_stock` contains a dictionary describing the ingredients in stock. The dictionary keys are `coffee`, `cream`, and `milk`.

The function should return:

- the name of the drink that can be prepared;
- the message "К сожалению, не можем предложить Вам напиток" ("Unfortunately, we cannot offer you a drink") if none of the preferences can be fulfilled.

If the order can be fulfilled, the quantities of available ingredients should decrease accordingly.

### Note

The solution should not include calls to the required functions.

### Example 1

__Input__
```python
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
```

__Output__
```plaintext
Эспрессо
К сожалению, не можем предложить Вам напиток
```

### Example 2

__Input__
```python
in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
```

__Output__
```plaintext
Капучино
Макиато
Эспрессо
```