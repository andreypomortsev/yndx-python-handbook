## [Polish Calculator — 2](../../../solutions/3.1/31_t.py)

Let's practice Reverse Polish Notation (RPN) further. Operations performed with one value are called unary, with two values — binary, with three values — ternary. Let's improve our calculator by adding support for the following operations:

- Binary operations:
   - \+ (addition),
   - \- (subtraction),
   - \* (multiplication),
   - / (integer division; for negative numbers, it works according to the same rules as in Python);

- Unary operations:
    - ~ (unary minus — changes the sign),
    - ! (factorial),
    - \# (cloning — push the value onto the stack twice);

- Ternary operation:\
    - @ (returns the same three values to the stack but in a different order: second, third, first).

### Input Format

A single line is entered containing space-separated integers and operation symbols. Together, they form a valid expression in Reverse Polish Notation, without division by zero or taking the factorial of a negative number.

### Output Format:

A single integer is output — the result of the expression's calculation.

### Note

In the first example, the stack looks like this as the string is read:

- 7
- 7 1
- 7 1 10
- 7 1 10 100
- 7 1 10 100 100
- 7 1 10 10000
- 7 10 10000 1
- 7 10 9999
- 7 10009
- 10016
- -10016

### Example 1

__Input__
```plaintext
7 1 10 100 # * @ - + + ~
```

__Output__
```plaintext
-10016
```

### Example 2

__Input__
```plaintext
10 15 - 7 *
```

__Output__
```plaintext
-35
```

### Note

`str.isdigit()` returns `False` for negative numbers.

### Example 3

__Input__
```plaintext
5 -1 2 + 4 * + 3 -
```

__Output__
```plaintext
6
```