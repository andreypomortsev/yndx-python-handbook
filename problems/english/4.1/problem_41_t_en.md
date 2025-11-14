## [Render Unto Caesar](../../../solutions/4.1/41_t.py)

Hooray! This is the final task!

In Ancient Rome, a special numeral system was used. To practice adding Roman numerals, write a function `roman`
that takes two natural numbers $a$ and $b$ and returns a string of the form:

ROMAN_A + ROMAN_B = ROMAN_SUM

### Note

Your solution must contain only functions.\
The solution must not include calls to the required functions.

<details>
<summary>Hint</summary>

You cannot modify the values passed to the function directly, but you can replace slices.

```python
result = roman(10, 9)
```

</details>

### Example 1

__Input__

```python
result = roman(10, 9)
```

__Output__

```python
result = 'X + IX = XIX'
```

### Example 2

__Input__

```python
result = roman(1499, 2500)
```

__Output__

```python
result = 'MCDXCIX + MMD = MMMCMXCIX'
```
