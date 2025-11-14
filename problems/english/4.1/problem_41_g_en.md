## [Max Max](../../../solutions/4.1/41_g.py)

Working with tables of numbers is an important skill, especially if you are analyzing data.
Let's try to find the largest number in such a table.

Write a function `max2D(matrix)` that takes a list of lists of integers and returns the maximum element.

### Note

The solution should not contain calls to the required functions.

<details>
<summary>Hint</summary>

We recommend using a list comprehension:

```python
max(max(row) for row in matrix)
```

</details>

### Example 1

__Input__

```python
result = max2D([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
```

__Output__

```plaintext
result = 2
```

### Example 2

__Input__

```python
result = max2D([[-5, -43, 72, 89], [-40, 92, -1, -73], [30, -75, 23, 94]])
```

__Output__

```plaintext
result = 94
```