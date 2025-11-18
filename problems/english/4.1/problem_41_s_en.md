## [Swapping Contents](../../../solutions/4.1/41_s.py)

Sometimes you need to swap the contents of two lists while keeping their references intact.\
That is, the objects remain the same, but their data is completely exchanged.

Create a function `swap(a, b)` that takes two lists and swaps their contents.\
The result must be visible in all variables that reference these lists.

### Note

Your solution must contain only functions.\
The solution must not contain calls to the required functions.

<details>
<summary>Hint</summary>

You cannot reassign the passed lists directly, but you can replace their slices.

```python
a = [1, 2, 3, 4, 5]
a[1:3] = [6, 7, 8]
print(a)  # [1, 6, 7, 8, 4, 5]
```

</details>

### Example

__Input__

```python
a = b = [1, 2]
c = d = [2, 1]
print(a, b, c, d)
swap(a, c)
print(a, b, c, d)
```

__Output__

```plaintext
[1, 2] [1, 2] [2, 1] [2, 1]
[2, 1] [2, 1] [1, 2] [1, 2]
```
