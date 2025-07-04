## [List of Squares 2](../../../solutions/3.3/33_b.py)

In this task, we continue working with list comprehensions, but now we’ll complicate the logic: the list of squares should be built regardless of the order of the values $a$ and $b$.

If $a < b$, the count goes forward. If $a > b$, the count goes backward. The result is a single list containing the squares of all numbers from $a$ to $b$ inclusive, in the corresponding order.

You are given the variables $a$ and $b$. Construct a list of squares of all integers from $a$ to $b$ inclusive — in ascending or descending order, depending on which value is greater.

### Note

The solution must contain nothing except a list comprehension.

<details>
<summary><h4>Hint</summary>

Use the solution to the previous task as a base and add a conditional expression `1 if a < b else -1` as the third parameter to `range`.

</details>

### Example 1

__Input__

```plaintext
a = 1
b = 5
```

__Output__

```plaintext
[1, 4, 9, 16, 25]
```

### Example 2

__Input__

```plaintext
a = 5
b = -4
```

__Output__

```plaintext
[25, 16, 9, 4, 1, 0, 1, 4, 9, 16]
```
