## [Mountain Search 2](../../../solutions/4.1/41_l.py)

Now let’s look at the terrain from above — as if you were flying in a plane.\
In front of you is a rectangular grid of elevations.\
Within this grid, there may also be “mountains” — points that are higher than all their neighbors in the 8 surrounding directions.

Create a function `find_mountains(data)` that takes a list of lists of numbers and returns a tuple of pairs with the indices of all mountains.\
Numbering starts from 1 (for both rows and columns).\
The edges of the grid are considered surrounded by mountains of infinite height, so there can be no mountains on the edges.

### Note

Your solution must contain only functions.\
There must be no calls to the required functions in the solution.

<details>
<summary>Hint</summary>

Describe the function:

```python
def find_mountains(data):
    ...
```

Compute the dimensions of the list:

```python
n = len(data)
m = len(data[0])
result = []
```

Iterate over the potential mountain points using the product iterator:

```python
for i, j in product(range(1, n - 1), range(1, m - 1)):
    if ...:
        result.append((i + 1, j + 1))  # +1 to account for required numbering
```

As a condition, we recommend using the all function:

```python
all(condition for k, t in product(range(i - 1, i + 2), range(j - 1, j + 2)))
```

where `condition` checks whether `(i, j)` is a mountain compared to `(k, t)`.

</details>

### Example 1

__Input__

```python
result = find_mountains([
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 1]
])
```

__Output__

```python
result = ((2, 2),)
```

### Example 2

__Input__

```python
result = find_mountains([
    [1, 1, 1, 1, 1, 1],
    [1, 2, 1, 5, 4, 1],
    [1, 1, 1, 3, 4, 3],
    [2, 3, 3, 1, 2, 3],
    [1, 2, 1, 3, 2, 1]
])
```

__Output__

```python
result = ((2, 2), (2, 4))
```
