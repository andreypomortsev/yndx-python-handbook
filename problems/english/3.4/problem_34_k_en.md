## [Numerical Rectangle 3.0](../../../solutions/3.4/34_k.py)

The kids in kindergarten are learning to count again, and the teacher decided to make it easier for them to master this new skill. For that, she wants to format the list of numbers in a special way.\
The kids are progressing quite quickly, so she needs a program that can construct number rectangles of the required size. Write a program that constructs a number rectangle of the required size.

### Input format

The first line contains the number $N$ — the height of the number rectangle.\
The second line contains the number $M$ — the width of the number rectangle.

### Output format:

You need to print the formed number rectangle of the required size.\
To make the rectangle look nice, each column must have the same width.

### Note

[itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product) is great for avoiding nested loops.

### Example 1

__Input__
```plaintext
2
3
```

__Output__
```plaintext
1 2 3
4 5 6
```

### Example 2

__Input__
```plaintext
4
6
```

__Output__
```plaintext
 1  2  3  4  5  6
 7  8  9 10 11 12
13 14 15 16 17 18
19 20 21 22 23 24
```