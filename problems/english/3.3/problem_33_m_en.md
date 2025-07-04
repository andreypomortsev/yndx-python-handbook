## [Dictionary Minimum](../../../solutions/3.3/33_m.py)

You are given a dictionary `data`, where the keys are words and the values are lists of numbers.

Write a single expression that finds the key with the smallest sum of values.
If there are several such keys, choose the lexicographically smallest one (i.e., the one that comes first alphabetically).

### Note

There should be nothing in your solution except an expression.

<details>
<summary><h4>Hint</h4></summary>

Use the following template:

```python
... for word, number in data.items() if ...
```

We recommend forming a sequence of tuples of the form (sum, word) from the dictionary.

In such a sequence, you can easily find the word with the smallest sum using the `min` function.

The result will be the second element of the resulting tuple.

</details>

### Example 1

__Input__
```plaintext
data = {'a': [1, 2, 3], 'b': [2, 3, 4, 5]}
```

__Output__
```plaintext
'a'
```

### Example 2

__Input__
```plaintext
data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}
```

__Output__
```plaintext
'b'
```
