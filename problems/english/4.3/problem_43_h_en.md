## [Fibonacci Generator](../../../solutions/4.3/43_h.py)

Fibonacci numbers form a very interesting sequence and are used in various mathematical problems. In this sequence, each subsequent element is the sum of the two previous ones. Mathematicians start this sequence with two ones, but we programmers are used to starting from zero.

Write the `fibonacci` generator, which sequentially returns a specified number of Fibonacci numbers according to "programmer rules."

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
print(*fibonacci(5))
```

__Output__
```plaintext
0 1 1 2 3
```

### Example 2

__Input__
```python
print(*fibonacci(10), sep=', ')
```

__Output__
```plaintext
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```