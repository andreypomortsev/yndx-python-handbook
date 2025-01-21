## [Territory of Evil](../../../solutions/2.2/22_r.py)

In ancient times, it was believed that if a certain area was shaped like a triangle, it contained terrible evil.

People assessed the risk of encountering evil based on the shape of the triangle:

- In an acute-angled triangle, the probability of encountering evil was very low (Russian - крайне мала);
- In an obtuse-angled triangle, it was high (Russian - велика);
- In a right-angled triangle, the probability was 100%.

Write a program that, based on the side lengths of the triangular area, determines the probability of encountering evil.

### Input Format

Three numbers — the side lengths of the triangular area.

### Output Format:

The probability of encountering evil according to the legend:

- крайне мала;
- велика;
- 100%.

### Example 1

__Input__
```plaintext
3
5
4
```

__Output__
```plaintext
100%
```

### Example 2

__Input__
```plaintext
6
3
4
```

__Output__
```plaintext
велика
```

## Solution

When comparing sides after floating-point calculations, it should be understood that the correct solution might fail due to calculation errors. Therefore, there are two ways to avoid this issue:

1. Use comparisons with an "acceptable error":
    ```python
    # Error threshold
    threshold = 1e-9

    a = 2.0000000001
    b = 2.0

    if abs(a - b) < threshold:
        print("The variables are equal")
    ```
2. Use the `isclose()` function from the `math` library, which works [similarly](https://docs.python.org/3/library/math.html#math.isclose).

    ```python
    import math

    # Absolute error threshold
    threshold = 1e-9

    a = 2.0000000001
    b = 2.0

    if math.isclose(a, b, abs_tol=threshold):
        print("The variables are equal")
    ```

    Use percentage error

    ```python
    import math

    # Relative error threshold
    threshold = 0.01

    a = 2.0000000001
    b = 2.0

    if math.isclose(a, b, rel_tol=threshold):
        print("The variables are equal")
    ```