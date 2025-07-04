## [Identifying Uniqueness](../../../solutions/3.3/33_k.py)

You've already completed 10 problems! You're doing great with lists and expressions.
If you want, take a short break, then come back — it only gets more interesting from here.

When working with data, it's important to be able to identify unique values — those that appear exactly once.

You are given a list called numbers.
Write an expression that creates a set of all numbers that appear in the list exactly once.

### Note

There should be nothing in your solution except an expression.

<details>
<summary><h4>Hint</h4></summary>

To check how many times a number appears in the list, you can use the `.count()` method.

</details>

### Example 1

__Input__
```plaintext
numbers = [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]
```

__Output__
```plaintext
{3, 4, 5}
```

### Example 2

__Input__
```plaintext
numbers = [-8, 7, -3, -2, 5, 0, 7, -2, -8, 6, -10, 4, -9, -9, 7]
```

__Output__
```plaintext
{0, 4, 5, 6, -10, -3}
```
