## [Merge Sort](../../../solutions/4.3/43_f.py)

We have already implemented the `merge` function, which can "merge" two sorted lists into one.\
Most commonly, it is used in the recursive merge sort algorithm.

Write a recursive function `merge_sort`, which sorts a list.

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions, except for recursive ones.\
The trace of the recursive function calls is not considered in the answer processing and is shown for example.

### Example 1

__Input__
```python
result = merge_sort([3, 2, 1])
```

__Output__
```plaintext
# Call merge_sort([3, 2, 1])
# Call merge_sort([3])
# Call merge_sort([2, 1])
# Call merge_sort([2])
# Call merge_sort([1])
result = [1, 2, 3]
```

### Example 2

__Input__
```python
result = merge_sort([3, 1, 5, 3])
```

__Output__
```plaintext
# Call merge_sort([3, 1, 5, 3])
# Call merge_sort([3, 1])
# Call merge_sort([3])
# Call merge_sort([1])
# Call merge_sort([5, 3])
# Call merge_sort([5])
# Call merge_sort([3])
result = [1, 3, 3, 5]
```