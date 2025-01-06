## [Race car 2.0](../../../solutions/2.3/23_p.py)

Let's revisit palindromes, which read the same in both directions. Write a program that checks if a number is a palindrome.

### Input Format

One natural number.

### Output Format:

"YES" if the number is a palindrome, otherwise "NO".

### Example 1

**Input**
```plaintext
1234
```

**Output**
```plaintext
NO
```

### Example 2

**Input**
```plaintext
123454321
```

**Output**
```plaintext
YES
```

## Approach to the Solution

The task is to check whether the given natural number is a palindrome. The "mirror symmetry" of the number is checked by comparing its left and right parts.

### Algorithm Logic

1. **Copy the Original Number**:
   - The input number is saved in a separate variable (`number_copy`) so that the original number remains unchanged for further computations during the algorithm.

2. **Determine the Most Significant Digit**:
   - First, compute the most significant digit of the number (`leftmost`), which defines the order of magnitude of the number (e.g., for 12345, it will be $10^5$).

3. **Cyclic Symmetry Check**:
   - The algorithm compares the first (most left) and the last (most right) digits of the number.
   - If these digits do not match, the number is not a palindrome, and the check terminates.
   - If the digits match, the algorithm "strips" the checked digits, shortening the number from both sides. To achieve this:
     - The first digit is removed by dividing the number by the most significant digit.
     - The last digit is removed by integer division of the number by 10.

4. **Narrowing Down the Digits**:
   - After each iteration, the order of magnitude of the most significant digit decreases by a factor of 100, as we remove one digit from each side.

5. **Result**:
   - If all digit pairs match, the number is a palindrome, and the result is `"YES"`.
   - If at least one pair of digits does not match, the result is `"NO"`.

### Optimizations

- **Step-by-Step Comparison of Digits**:
  Instead of reversing the entire number and comparing strings, the algorithm works with the current digits, saving memory.

- **Termination on Mismatch**:
  The algorithm terminates early if a mismatch is found between any pair of digits, minimizing unnecessary operations.

### Example Run of the Algorithm

### Example 1

**Input:**
```plaintext
1234
```

**Output:**
```plaintext
NO
```

- Most significant digit: $10^3 = 1000$.
- Comparison: $1 \neq 4$.

The number is not a palindrome.

### Example 2

**Input:**
```plaintext
123454321
```

**Output:**
```plaintext
YES
```

- Most significant digit: $10^8 = 100000000$.
- Iterative comparison:
  - $1 = 1$, number becomes $2345432$, most significant digit $10^6$
  - $2 = 2$, number becomes $34543$, most significant digit $10^4$
  - $3 = 3$, number becomes $454$, most significant digit $10^2$
  - $4 = 4$, number becomes $5$, most significant digit $10^0$

The number is a palindrome.

### Note

*We don't need to do anything with the center digit in numbers with an odd number of digits (e.g., `5` in 1234`5`4321), as it remains in place when the number is reversed and doesn't affect the result of the palindrome check.*