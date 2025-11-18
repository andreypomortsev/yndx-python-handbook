## [Mountain Search](../../../solutions/4.1/41_k.py)

You're halfway through the collection—great work!

Imagine you're looking at the horizon line.\
In front of you is a sequence of numbers representing heights.\
Sometimes there are "mountains" among them—points that are taller than their closest neighbors.

Write a function `find_mountains(heights)` that accepts a list of heights and returns a tuple of the indices of all mountains. Indexing starts from 1.

We assume the edges of the list are surrounded by mountains of infinite height, so only the inner points are compared.

### Note

Your solution must contain only functions.\
The solution must not include calls to the required functions.

<details>
<summary>Hint</summary>

You can iterate over the elements like this:

```python
for index, (left, middle, right) in enumerate(zip(data, data[1:], data[2:]), 2):
    ...
```

where `data` is the passed list.

This way, on each iteration you'll have the current element `middle`, its position `index`, and both neighbors `left` and `right`.

</details>

### Example 1

__Input__
```python
result = find_mountains([1, 2, 1, 4, 1])
```

__Output__
```python
result = (2, 4)
```

### Example 2

__Input__
```python
result = find_mountains([5, 1, 10, 2, 3, 4, 3, 20])
```

__Output__
```python
result = (3, 6)
```
