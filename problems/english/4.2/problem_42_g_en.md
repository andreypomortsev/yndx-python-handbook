## [On Air — 'Experiments' Section](../../../solutions/4.2/42_g.py)

The lab assistants are conducting an experiment and have requested the development of a data processing system. The experiment results should be pairs of rational numbers.

The required functions are:

- `enter_results(first, second, ...)` — adds data for one or more results (it is guaranteed that the number of parameters will be even);
- `get_sum()` — returns a pair of sums of the experiment results;
- `get_average()` — returns a pair of arithmetic mean values of the experiment results.

All calculations are performed with an accuracy of two decimal places.

### Note

The solution must not include calls to the required functions.

### Example 1

__Input__
```python
enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
```

__Output__
```plaintext
(9, 12) (3.0, 4.0)
(10, 14) (2.5, 3.5)
```

### Example 2

__Input__
```python
enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())
```

__Output__
```plaintext
(48.7, 40.13) (24.35, 20.07)
(53.9, 47.43) (17.97, 15.81)
(58.27, 54.7) (9.71, 9.12)
```