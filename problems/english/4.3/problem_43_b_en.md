## [Recursive Digits Summator](../../../solutions/4.3/43_b.py)

Recursion is a great way to eliminate loops, especially `while`. Let's revisit one of our old tasks and modernize it.

Write a function `recursive_digit_sum` that finds the sum of all digits of a natural number.

### Note

Your solution should contain only functions.\
There should be no calls to the required functions, except for recursive calls.\
The trace of the recursive function calls in the answer is not considered and is shown for example purposes.

### Example 1

__Input__
```python
result = recursive_digit_sum(123)
```

__Output__
```plaintext
# Calling recursive_digit_sum(123)
# Calling recursive_digit_sum(12)
# Calling recursive_digit_sum(1)
# Calling recursive_digit_sum(0)
result = 6
```

### Example 2

__Input__
```python
result = recursive_digit_sum(7321346)
```

__Output__
```plaintext
# Calling recursive_digit_sum(7321346)
# Calling recursive_digit_sum(732134)
# Calling recursive_digit_sum(73213)
# Calling recursive_digit_sum(7321)
# Calling recursive_digit_sum(732)
# Calling recursive_digit_sum(73)
# Calling recursive_digit_sum(7)
# Calling recursive_digit_sum(0)
result = 26
```