## [Function Extremum](../../../solutions/6.2/62_j.py)

In mathematics, an extremum refers to the maximum or minimum value of a function within a given range.

Typically, mathematicians use differentiation to find the extremum of a function. However, we can bypass this laborious process with a shortcut.

Write three functions:

- `values(func, start, end, step)`, which generates a _Series_ of function values at points within the given range and takes:
    - A single-variable function.
    - The start of the range.
    - The end of the range.
    - The step size for calculation.
- `min_extremum(data)` returns the point at which the minimum is reached within the range.
- `max_extremum(data)` returns the point at which the maximum is reached within the range.

### Note

Your solution should only contain functions.\
Do not call the required functions in your solution.

### Example

__Input__
```python
data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
```

__Output__
```plaintext
-1.500000e+00    0.25
-1.400000e+00    0.16
-1.300000e+00    0.09
-1.200000e+00    0.04
-1.100000e+00    0.01
-1.000000e+00    0.00
-9.000000e-01    0.01
-8.000000e-01    0.04
-7.000000e-01    0.09
-6.000000e-01    0.16
-5.000000e-01    0.25
-4.000000e-01    0.36
-3.000000e-01    0.49
-2.000000e-01    0.64
-1.000000e-01    0.81
 1.332268e-15    1.00
 1.000000e-01    1.21
 2.000000e-01    1.44
 3.000000e-01    1.69
 4.000000e-01    1.96
 5.000000e-01    2.25
 6.000000e-01    2.56
 7.000000e-01    2.89
 8.000000e-01    3.24
 9.000000e-01    3.61
 1.000000e+00    4.00
 1.100000e+00    4.41
 1.200000e+00    4.84
 1.300000e+00    5.29
 1.400000e+00    5.76
 1.500000e+00    6.25
 1.600000e+00    6.76
 1.700000e+00    7.29
dtype: float64
-0.9999999999999996
1.7000000000000028
```