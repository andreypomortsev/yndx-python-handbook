## [Digital Squeeze](../../../solutions/3.3/33_g.py)

Let's continue practicing list comprehensions.

This time, you need to find all the digits in a string.
You will be given a variable `text` — a string that may contain any characters.
You need to extract all the digits and collect them into a single string, preserving their order of appearance.

### Note

There should be nothing in your solution except a list comprehension.

<details>
<summary><h4>Hint</h4></summary>

Use the following template:

```python
''.join(... for ... in text if ...)
```

</details>

### Example 1

__Input__
```plaintext
text = '33 cows,\n' + \
    '33 cows,\n' + \
    '33 cows -\n' + \
    'A fresh line.\n' + \
    '33 cows,\n' + \
    'A new poem was born,\n' + \
    'Like a glass of fresh milk.\n' + \
    'A new poem was born,\n' + \
    'Like a glass of fresh milk.\n'
```

__Output__
```plaintext
'33333333'
```

### Example 2

__Input__
```plaintext
text = '2 + 2 = 4'
```

__Output__
```plaintext
'224'
```
