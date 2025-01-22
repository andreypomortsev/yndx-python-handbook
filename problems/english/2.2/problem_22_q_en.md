## [Root of Evil](../../../solutions/2.2/22_q.py)

Not everyone likes mathematics, and some even consider it true evil incarnate, though it is unavoidable. For example, Python was originally developed for solving mathematical problems, so let's use it to find the roots of a quadratic equation.

### Input Format

You are given 3 real numbers $a$, $b$, $c$ — the coefficients of a quadratic equation in the form:

$ax^2+bx+c=0$

### Output Format:

- If the equation has no solutions, print "No solution".
- If the equation has a finite number of solutions, print them in ascending order with a precision of two decimal places.
- If the equation has an infinite number of solutions, print "Infinite solutions".

### Example 1

__Input__
```plaintext
1
-2
1
```

__Output__
```plaintext
1.00
```

### Example 2

__Input__
```plaintext
3.5
-2.4
-7.3
```

__Output__
```plaintext
-1.14 1.83
```

### Solution

To avoid a **RuntimeError** on the third test, first handle the cases where the coefficients might be zero and only then calculate the discriminant.

### [Video on YouTube with problem overview](https://www.youtube.com/live/c67zB3FWLOs?si=Ee1N3AhF2CB9n4J4&t=2250)