## [Take care of the pennies](../../../solutions/4.1/41_d.py)

The program can process any data - even the contents of a wallet.
Imagine that you have a list of banknotes and coins. You need to select only the small change from it - everything that is less than 100 rubles.

Write a function take_small(money) that takes a list of denominations and returns a new list - only with those values that are less than 100.
The order of the elements must be preserved.

### Note

The initial list should not be changed.
Your solution should contain only functions.

<details>
<summary>Hint</summary>

Describe the function:

```python
def take_small(money):
    ...
```

Create a list and transfer only the required values:

```python
result = []
for ... in money:
    if ...:
        result.append(...)
return result
```

Or you can use a list comprehension:

```python
return [... for ... in money if ...]
```

</details>

### Example 1

__Input__
```python
money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]
result = take_small(money)
```

__Output__
```python
result = [1, 5, 0.5, 0.05, 10, 25, 1, 2, 0.1, 5, 0.01]
```

### Example 2

__Input__
```python
data = [0.01, 0.01, 500, 2000, 5000, 0.05, 1, 200, 0.1, 2000, 1000, 10, 25, 0.05, 10, 2000, 500, 5000, 0.01, 200, 2, 1000, 0.5, 5000, 10, 0.5, 5, 1]
result = take_small(data)
```

__Output__
```python
result = [0.01, 0.01, 0.05, 1, 0.1, 10, 25, 0.05, 10, 0.01, 2, 0.5, 10, 0.5, 5, 1]
```