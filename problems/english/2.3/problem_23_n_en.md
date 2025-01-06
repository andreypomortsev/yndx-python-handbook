## [Simple Task](../../../solutions/2.3/23_n.py)

One of the most interesting types of numbers in mathematics is prime numbers. They share the property that they can only be divided by 1 and themselves. They are still studied by scientists around the world. They are also used in computing: algorithms for encrypting data can be written using them. Let's write a program to determine whether a given number is prime or not.

### Input Format

A single natural number is given as input.

### Output Format:

You need to output the message YES if the number is prime, otherwise NO.

### Note

A prime number is defined as a number that has exactly two divisors.

### Example 1

**Input**
```plaintext
1
```

**Output**
```plaintext
NO
```

### Example 2

**Input**
```plaintext
67
```

**Output**
```plaintext
YES
```

## Approach to the Problem

To determine whether a number is prime, we can use an optimized method of divisibility checking. Here are the steps of the algorithm:

1. **Handle exceptions**:
   - If the number is less than or equal to 1, it is not prime. Prime numbers are those that have exactly two divisors (1 and the number itself).
   - If the number is 2 or 3, it is prime (both are the smallest prime numbers).

2. **Check divisibility by 2 and 3**:
   - Numbers divisible by 2 or 3 are not prime. This is a basic optimization that allows us to exclude many composite numbers.

3. **Check divisibility with step 6**:
   - If the number is not divisible by 2 or 3, we can check for divisibility by numbers of the form $6k \pm 1$ (where $k$ is an integer). This is because all other numbers are either divisible by 2 or 3.
   - The check is performed for numbers from 5 to $\sqrt{n} + 1$, as if $n$ is divisible by $d$ where $d > \sqrt{n}$, then $n$ must also be divisible by $d'$ where $d' < \sqrt{n}$.