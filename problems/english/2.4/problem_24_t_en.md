## [Mathematical Benefit](../../../solutions/2.4/24_t.py)

Mathematician Vitaliy Evgenievich pondered over the question of the benefit of numeral systems. He decided that a "beneficial" numeral system would be the one in which a number has the highest sum of digits. Write a program that, given a number, determines the base of the numeral system with the maximum benefit.

### Input format

One natural number.

### Output format:

One natural number from the range [2; 10] — the base of the numeral system with the maximum benefit.
If there are multiple bases with the same sum of digits, choose the smallest base.

### Note

You can read more about numeral systems [here](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%81%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F).

### Example 1

__Input__
```plaintext
12
```

__Output__
```plaintext
7
```

### Example 2

__Input__
```plaintext
52
```

__Output__
```plaintext
9
```

### Approach to Solution

1. **Understanding the base system:**
   - For a given number, its representation in a numeral system depends on the base. For example, the number 12 in base 7 is represented as `15`, and the sum of its digits is `1 + 5 = 6`.
   - For each base in the range from 2 to 10, we need to convert the number into that base and compute the sum of its digits.

2. **Converting the number to a different base:**
   - We can repeatedly divide the number by the base, storing the remainders (which correspond to the digits in the given base) until the number becomes zero.

3. **Computing the sum of digits:**
   - For each base, after converting the number, compute the sum of the digits.

4. **Finding the base with the maximum sum:**
   - Track the base that gives the highest sum of digits. If there are ties, return the smallest base.

This approach ensures that we correctly compute and compare the sum of digits for all bases in the range [2; 10].