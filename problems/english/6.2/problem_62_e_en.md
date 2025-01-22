## [Long Words](../../../solutions/6.2/62_e.py)

Data filtering is one of the key tasks in data analysis.

Write a function `get_long` that takes a series in the format of the first task and filters it by the named parameter `min_length` (default value 5).

### Note

Your solution should contain only functions.\
There should be no calls to the required functions in the solution.

### Example 1

__Input__
```python
data = pd.Series([3, 5, 6, 6], ['world', 'python', 'hello', 'yandex'])
filtered = get_long(data)
print(data)
print(filtered)
```

__Output__
```plaintext
world     3
python    5
hello     6
yandex    6
dtype: int64
python    5
hello     6
yandex    6
dtype: int64
```

### Example 2

__Input__
```python
data = pd.Series([3, 5, 6, 6], ['world', 'python', 'hello', 'yandex'])
filtered = get_long(data, min_length=6)
print(data)
print(filtered)
```

__Output__
```plaintext
world     3
python    5
hello     6
yandex    6
dtype: int64
hello     6
yandex    6
dtype: int64
```