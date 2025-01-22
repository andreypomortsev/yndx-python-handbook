## [Numeric Square](../../../solutions/2.4/24_s.py)

Unfortunately, the snakes have also become boring to the children, so now the teacher needs a new program. Write a program that constructs a numeric square of the required size.

### Input format

The first line contains the number $N$ — the height and width of the numeric square.

### Output format:

You need to print the generated numeric square of the required size.
To make the square neat, each column should have the same width.

### Example 1

__Input__
```plaintext
3
```

__Output__
```plaintext
1 1 1
1 2 1
1 1 1
```

### Example 2

__Input__
```plaintext
5
```

__Output__
```plaintext
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
```

### Approach to Solution

1. **Understanding the structure of the square:**
   - The square has $N$ rows and $N$ columns.
   - The numbers in the square form concentric layers where the outermost layer is filled with 1's, the next layer is filled with 2's, and so on, with the center being filled with the largest number.

2. **Constructing the square:**
   - As I've already written [here](https://t.me/handbook_python/11/32431) (you can use built-in translator), for each position in the square, calculate the number based on its distance from the nearest edge. This can be done by finding the minimum of the distances from the current position to the four edges (top, bottom, left, right).
   - The number at each position will be `min(distance from edge)`.

3. **Printing the square:**
   - Ensure that the numbers in each column are aligned by formatting the output, such as using string formatting to make all numbers have the same width.

This approach ensures that the square is generated correctly for any given $N$ and printed in a neat format.