## [RLE](../../../solutions/3.1/31_r.py)

RLE stands for "run-length encoding." It is a way of shorthand notation for a sequence of things (in this case, digits). For a group of consecutive identical digits (a run), the digit itself and the length of this group (run length) are recorded. For example, `99999` becomes `9 5` ("nine five times"), and so on. RLE is widely used in various fields. Write a program that encodes a string of digits using RLE.

### Input Format

A string of digits with a length of at least 1.

### Output Format:

Pairs of the digit itself and the number of consecutive repetitions of the digit in the input string, as described in the problem and shown in the example.

### Example 1

__Input__
```plaintext
010000100001111111110111110000000000000011111111
```

__Output__
```plaintext
0 1
1 1
0 4
1 1
0 4
1 9
0 1
1 5
0 14
1 8
```

### Example 2

__Input__
```plaintext
0110000000100001000
```

__Output__
```plaintext
0 1
1 2
0 7
1 1
0 4
1 1
0 3
```