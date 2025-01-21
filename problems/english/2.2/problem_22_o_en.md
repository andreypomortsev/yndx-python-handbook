## [Lord of Numbers: The Return of Caesar](../../../solutions/2.2/22_o.py)

To defeat the evil, there is only one step left — destroy Zeron's lair.

To do this, we need to create a three-digit magical number that will be stronger than Zeron's two two-digit protective numbers.

The simplest way to create a strong number:

- Take the largest digit from all the protective numbers.
- Take the smallest digit from all the protective numbers.
- Place the sum of the remaining digits (without carrying over the digits) in the middle.

Help us defeat the evil!

### Input format

Two lines, each containing one of Zeron's protective numbers.

### Output format:

A single three-digit number that will lead to victory.

### Example 1

__Input__
```plaintext
31
11
```

__Output__
```plaintext
321
```

### Example 2

__Input__
```plaintext
49
17
```

__Output__
```plaintext
911
```