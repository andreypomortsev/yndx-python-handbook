## [Long Sorting](../../../solutions/4.2/42_h.py)

Write a `lambda` expression to sort a list of words first by length, then alphabetically, ignoring case.

### Note

The solution must consist only of the expression.

### Example 1

__Input__
```python
string = 'мама мыла раму'
print(sorted(string.split(), key=<your expression>))
```

__Output__
```plaintext
['мама', 'мыла', 'раму']
```

### Example 2

__Input__
```python
string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=<your expression>))
```

__Output__
```plaintext
['во', 'Python', 'многих', 'Яндекс', 'проектах', 'использует']
```