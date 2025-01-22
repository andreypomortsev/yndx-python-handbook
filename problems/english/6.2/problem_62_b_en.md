## [Lengths of All Words by Parity](../../../solutions/6.2/62_b.py)

This time, think of a function `length_stats` that takes a text and returns a pair of _Series_ objects with words as indices and their lengths as values.

All words in the text should be converted to lowercase, punctuation marks and digits should be removed, and the words should be sorted lexicographically.

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)
```

__Output__
```plaintext
Series([], dtype: int64)
мама    4
мыла    4
раму    4
dtype: int64
```

### Example 2

__Input__
```python
odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)
```

__Output__
```plaintext
домик    5
и        1
лес      3
dtype: int64
зверушка    8
опушка      6
странный    8
dtype: int64
```