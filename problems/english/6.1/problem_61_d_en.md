## [Non-arithmetic mean](../../../solutions/6.1/61_d.py)

The geometric mean of several positive real numbers is the number that can replace each of these numbers such that their product remains unchanged.

The formula for the geometric mean of $n$ numbers is as follows:

$$
G(x_1, x_2, \dots, x_n) = \sqrt[n]{x_1 \cdot x_2 \dots x_n} = \left( \prod_{i=1}^n x_i \right)^{\frac{1}{n}}
$$

### Input format

A sequence of rational numbers separated by spaces is entered.

### Output format

A single number — the geometric mean of the given numbers.

### Example 1

__Input__
```plaintext
1 2 3 4 5
```

__Output__
```plaintext
2.605171084697352
```

### Example 2

__Input__
```plaintext
1.1 1.2 1.3 1.4 1.5
```

__Output__
```plaintext
1.292252305460076
```