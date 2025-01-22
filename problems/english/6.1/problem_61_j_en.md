## [Stairs](../../../solutions/6.1/61_j.py)

Write a function `stairs` that takes a vector and returns a matrix where each row is a copy of the vector with an offset.

### Note

Your solution should contain only functions.\
The solution should not include calls to the required functions.

### Example 1

__Input__
```python
print(stairs(np.arange(3)))
```

__Output__
```plaintext
[[0 1 2]
 [2 0 1]
 [1 2 0]]
```

### Example 2

__Input__
```python
print(stairs(np.arange(5)))
```

__Output__
```plaintext
[[0 1 2 3 4]
 [4 0 1 2 3]
 [3 4 0 1 2]
 [2 3 4 0 1]
 [1 2 3 4 0]]
```

## Approach

I use [advanced indexing in NumPy](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing) to create a matrix with cyclic shifts of elements.

1. First, I create an index array from 0 to $n-1$ using `np.arange(n)`.
2. For each shift, I create an index array using `np.arange(n) - i`, where $i$ is the number of shifts for each row.
3. In _NumPy_, negative indices work like indices from the end of the array, e.g., -1 refers to the last element. This allows us to cyclically "wrap" the indices.

### Why the solution works:

- Negative indexing automatically "wraps" the indices, so there's no need to perform additional operations.
- This solution is efficient for the task as each shift is performed in constant time.

### Advantage:

- No unnecessary array copies are created, as indexing works directly on the original data.

### Code to check memory usage

Make sure you have installed:

- `numpy`
- `memory_profiler`

#### Advanced Indexing

```python
import numpy as np
from memory_profiler import profile


# Solution using advanced indexing
@profile
def stairs_advanced(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array([row[(np.arange(n) - i)] for i in range(n)])
    return result


if __name__ == "__main__":
    row = np.arange(10000)
    print("RAM usage for the advanced indexing solution:")
    stairs_advanced(row)

```

#### Solution with np.roll

```python
import numpy as np
from memory_profiler import profile


# Solution using np.roll
@profile
def stairs_roll(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    return result


if __name__ == "__main__":
    row = np.arange(10000)
    print("RAM usage for the np.roll solution:")
    stairs_roll(row)

```

### Results

_The measurements were made on an Apple MacBook Pro M1 Pro 16 Gb_

#### Advanced Indexing

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     31.0 MiB     31.0 MiB           1   @profile
     7                                         def stairs_advanced(row: np.array) -> np.ndarray:
     8     31.0 MiB      0.0 MiB           1       n = row.shape[0]
     9   1256.9 MiB   1225.9 MiB       10001       result = np.array([row[(np.arange(n) - i)] for i in range(n)])
    10   1256.9 MiB      0.0 MiB           1       return result
```

#### np.roll

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     30.9 MiB     30.9 MiB           1   @profile
     7                                         def stairs_roll(row: np.array) -> np.ndarray:
     8     30.9 MiB      0.0 MiB           1       n = row.shape[0]
     9   1364.0 MiB   1333.1 MiB       20001       result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    10   1364.0 MiB      0.0 MiB           1       return result
```

### Disadvantages of `np.roll`:

- Less flexibility: `np.roll` is limited to cyclic shifting, whereas my solution allows easier customization of the shift type if needed.
- Redundancy: When using `np.roll`, each shift requires recalculating the entire array, which may be less efficient for some cases.