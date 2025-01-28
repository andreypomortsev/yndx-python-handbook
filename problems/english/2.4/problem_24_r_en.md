## [New Year's spirit 2.0](../../../solutions/2.4/24_r.py)

Colleagues of the mathematician want to delight him again by creating mathematical Christmas trees to decorate the scientist's office. Help them by writing a program that builds a mathematical Christmas tree based on the entered number.

### Input format

A single natural number is entered — the number of numbers in the mathematical Christmas tree.

### Output format:

The required New Year's Christmas tree.

### Example 1

__Input__
```plaintext
14
```

__Output__
```plaintext
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
```

### Example 2

__Input__
```plaintext
6
```

__Output__
```plaintext
  1  
 2 3 
4 5 6
```

### Approach to Solution

1. **Determine the number of rows of the tree:**
   - Use the formula for calculating triangular numbers: $t = \frac{n \cdot (n + 1)}{2}$, where $t$ is the total number of numbers, and $n$ is the number of rows.
   - Find $n$ using the inverse formula: $n = \frac{-1 + \sqrt{1 + 8 \cdot t}}{2}$.
   - Round $n$ up to the nearest integer to account for all numbers in $t$.

2. **Formatting the output:**
   - For each number in a row, take its length into account to properly align the numbers in the center.
   - Calculate the maximum row width (`formatter`) to ensure correct output formatting.

3. **Generate the tree:**
   - Use two loops that together iterate from 0 to $t$.
   - In the inner loop, add numbers sequentially to the row, then print the result after exiting the loop.
   - Format the string using the `formatter` width for centering.
   - The outer loop is responsible for the total number of rows.