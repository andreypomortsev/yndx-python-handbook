## [Filtering 101](../../../solutions/3.3/33_c.py)

We’re moving from list construction to value filtering.
Now your goal is to select only those numbers from the range that are divisible by a given value without a remainder.

You are given three variables: $a$, $b$, and $d$.
Construct a list of all numbers divisible by $d$ within the range from $a$ to $b$ inclusive.

Use a single list comprehension to build a list of all numbers from $a$ to $b$ that are divisible by $d$ without a remainder.

### Note

The solution must contain nothing except a list comprehension.

<details>
<summary><h4>Hint</summary>

The first number in the range divisible by $d$ can be found by computing `(a + d - 1) // d * d` or `a + d - a % d`.

Don’t forget to set the step to $d$.

</details>

### Example 1

__Input__

```plaintext
a = 1
b = 5
d = 2
```

__Output__

```plaintext
[2, 4]
```

### Example 2

__Input__

```plaintext
a = -9
b = 15
d = 3
```

__Output__

```plaintext
[-9, -6, -3, 0, 3, 6, 9, 12, 15]
```
