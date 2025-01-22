## [Fractions v0.1](../../../solutions/5.2/52_d.py)

You may have already noticed that floating-point numbers (float) are not precise enough for some tasks. For more accurate mathematical calculations, rational fractions described by a numerator and a denominator are sometimes used.

Let's start developing the `Fraction` class, which implements the proposed fractions.

Provide the ability to initialize a fraction using two integers or a string in the format \<numerator>/\<denominator>.\
In cases where the numerator and denominator have a common divisor, the fraction should be simplified.

Also, implement the following methods:

- `numerator()` — returns the value of the numerator;
- `numerator(number)` — changes the value of the numerator and simplifies the fraction if necessary;
- `denominator()` — returns the value of the denominator;
- `denominator(number)` — changes the value of the denominator and simplifies the fraction if necessary;
- `__str__` — returns the string representation of the fraction in the format \<numerator>/\<denominator>;
- `__repr__` — returns the description of the object in the format Fraction(\<numerator>, \<denominator>).

### Note

Let's assume that the user knows about the prohibition of division by zero.\
All numbers in this task will be positive.\
All fields and methods not required for the task should be encapsulated (named with leading underscores).

Your solution should only contain classes and functions.\
The solution should not contain any initialization calls for the required classes.

### Example 1

__Input__
```python
fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
```

__Output__
```plaintext
1/3 Fraction(1, 3)
1/2 Fraction(1, 2)
```

### Example 2

__Input__
```python
fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
```

__Output__
```plaintext
1/70 Fraction(1, 70)
1 7
1 2
```