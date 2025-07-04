## [Error Detection](../../../solutions/3.3/33_n.py)

Sometimes, data contains errors — for example, duplicates where there shouldn't be any.
Let's learn how to quickly find such cases using dictionaries and expressions.

You are given a dictionary `data`, where the keys are words and the values are lists of numbers.

Write an expression to create a set of keys whose values contain duplicates.

### Note

There should be nothing in your solution except an expression.

<details>
<summary><h4>Hint</h4></summary>

If there are duplicates, the length of the list and the set built from it will be different.

</details>

### Example 1

__Input__
```plaintext
data = {'a': [1, 2, 1], 'b': [2, 3, 2, 5, 1]}
```

__Output__
```plaintext
{'a', 'b'}
```

### Example 2

__Input__
```plaintext
data = {'a': [1, 2, 3], 'b': [5, 2, 5], 'c': [7, 15, 3]}
```

__Output__
```plaintext
{'b'}
```
