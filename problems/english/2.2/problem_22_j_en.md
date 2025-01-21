## [Best defense is encryption](../../../solutions/2.2/22_j.py)

Kolya was afraid that Anya would peek at all his passwords in the notebook, so he decided to encrypt them. For this, he takes the original password — a three-digit number — and creates a new number according to the following rules:

- The sum of the digits in the two least significant places (tens and ones) is found.
- The sum of the digits in the two most significant places (hundreds and tens) is found.
- These two sums, written one after the other in non-increasing order, form a new number.

Help implement the encryption algorithm.

### Input format

One three-digit number.

### Output format:

The result of encryption.

### Example 1

__Input__
```plaintext
123
```

__Output__
```plaintext
53
```

### Example 2

__Input__
```plaintext
741
```

__Output__
```plaintext
115
```

## Solution

---

### Number Breakdown
1. Read the three-digit number from the input.  
2. Break it into individual digits:  
   - Hundreds: `n // 100`  
   - Tens: `n // 10 % 10`  
   - Ones: `n % 10`.  

---

### Sum Calculation
1. Calculate the sum of the digits in the least significant places (tens and ones):  
   ```python
   second_sum = tens + ones
   ```  
2. Calculate the sum of the digits in the most significant places (hundreds and tens):  
   ```python
   first_sum = hundreds + tens
   ```  

---

### Checking the Order of Sums
1. If the sum of the least significant places is greater than the sum of the most significant places, swap them:  
   ```python
   if first_sum < second_sum:
       first_sum, second_sum = second_sum, first_sum
   ```

---

### Forming the Result
1. Determine if the sum of the least significant places is greater than 9, and based on that calculate the power for the multiplier:  
   ```python
   condition = second_sum > 9
   power = 1 + condition
   ```  
2. Calculate the multiplier as `10` raised to the power of `power`:  
   ```python
   multiplier = 10**power
   ```  
3. Form the final number by multiplying the first sum by the multiplier and adding the second sum:  
   ```python
   answer = first_sum * multiplier + second_sum
   ```  

---

### Example Execution (for `123`)
1. Break the number:  
   - Hundreds = `1`, Tens = `2`, Ones = `3`.  
2. Calculate the sums:  
   - Sum of the least significant places = `2 + 3 = 5`.  
   - Sum of the most significant places = `1 + 2 = 3`.  
3. Swap the sums because `5 > 3`:  
   - `first_sum = 5`, `second_sum = 3`.  
4. Form the result:  
   - `second_sum <= 9`, so:
     ```python
     answer = first_sum * 10 + second_sum = 5 * 10 + 3 = 53
     ```  
5. Output: `53`.