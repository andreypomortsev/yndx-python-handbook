## [Maximum Product](../../../solutions/3.3/33_l.py)

You are given a set called `numbers`.
Write a single expression that finds the maximum product of two distinct numbers from this set.

### Note

There should be nothing in your solution except an expression.

<details>
<summary><h4>Hint</h4></summary>

Let's not focus on the optimal solution.

To iterate over all possible pairs, you can use nested loops in an expression:

```python
(... for first in numbers for second in numbers if first != second)
```

</details>

### Example 1

__Input__
```plaintext
numbers = {1, 2, 3, 4, 5}
```

__Output__
```plaintext
20
```

### Example 2

__Input__
```plaintext
numbers = {2, 4, 5, 7, -10, -8, 10, -9, -1}
```

__Output__
```plaintext
90
```
