## [Lengths of All Words - 2](../../../solutions/6.2/62_a.py)

Write a function `length_stats` that takes a text and returns a _Series_ object with words as indices and their lengths as values.

All words in the text should be converted to lowercase, punctuation marks and digits should be removed, and the words should be sorted lexicographically.

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
print(length_stats('Мама мыла раму'))
```

__Output__
```plaintext
мама    4
мыла    4
раму    4
dtype: int64
```

### Example 2

__Input__
```python
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
```

__Output__
```plaintext
домик       5
зверушка    8
и           1
лес         3
опушка      6
странный    8
dtype: int64
```