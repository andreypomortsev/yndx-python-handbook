## [Numeric Fragmentation](../../../solutions/4.1/41_h.py)

Suppose you have a list of numbers and want to split it into increasing fragments—segments where every next number is greater than the previous one.\
Such a task can be useful when analyzing sequences, graphs, or user activity.

Write a function `fragments(numbers)` that takes a list of integers and returns a list of nested lists, each representing an increasing segment of the original sequence.

### Note

Your solution must contain only functions.\
The solution must not include calls to the required functions.

<details>
<summary>Hint</summary>

Keep in mind that a single-element list is also an increasing sequence.

Create a list of lists and place the first number in it. Iterate over the remaining numbers:

- if the number is greater than the previous one, append it to the last inner list;
- if the number is less than or equal to the previous one, start a new inner list with this number.

</details>

### Example 1

__Input__
```python
result = fragments([0, 4, 5, -9, -6, 3, 2, 3, 4, 9])
```

__Output__
```python
result = [[0, 4, 5], [-9, -6, 3], [2, 3, 4, 9]]
```

### Example 2

__Input__
```python
result = fragments([-4, -2, 5, 0, 3, 7, -8, -2, 6, 7, 6, 8, 10, 5, 7, 8])
```

__Output__
```python
result = [[-4, -2], [5, 0, 3, 7], [-8, -2, 6, 7, 6, 8, 10], [5, 7, 8]]