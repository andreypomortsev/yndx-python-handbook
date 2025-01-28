## [Race Car](../../../solutions/2.2/22_g.py)

There is an interesting concept called a palindrome — a number, word, sentence, etc., that reads the same both from left to right and from right to left.

Write a program that checks if a number is a palindrome.

### Input format

One four-digit number.

### Output format:

YES if the number is a palindrome, otherwise — NO.

### Example 1

__Input__
```plaintext
1234
```

__Output__
```plaintext
NO
```

### Example 2

__Input__
```plaintext
2332
```

__Output__
```plaintext
YES
```

## Solution

The simplest way to check for a palindrome is to reverse the string (its half) using slices.

```python
"racecar" == "racecar"[::-1]
```

But the task specifies that the input will be a *number* of *known length*, so it can be broken down into digits and the first compared with the last, and the second with the second last.
To break the number into digits, use `//` and `%`.

To get the first digit of a 4-digit number, divide it by 1000 using integer division; to get the last digit, use `%`, which gives the remainder of the division by 10. Using these operators, find the remaining digits and compare them — only if both pairs are equal, it is a palindrome.