## [Polish Calculator](../../../solutions/3.1/31_s.py)

Write a program that calculates an expression written in Reverse Polish Notation (RPN).

In RPN, there are no parentheses or operator precedence ("multiplication before addition").

To read an expression in this format, you need to process the expression strictly sequentially. The input values are successively added to the stack. When an operator symbol is encountered, the last two values added to the stack are removed, the operation is performed with them, and the result is returned to the stack.

If the order of values matters for the operation, the first value to be used is the one that was deeper in the stack. In particular, if the operation is subtraction, the second-to-last number in the stack is subtracted by the last one, not the other way around.

Initially, the stack is empty, and after completing the calculation of the expression, there should be one value left in it — the result of the calculation.

The first example should be read as follows: the values 7, 2, and 3 are sequentially added to the stack, and then the operator `*` is encountered. The values 2 and 3 are removed, multiplied, and the result 6 is placed back into the stack. The next operator removes the two remaining values 7 and 6 from the stack, subtracts one from the other, and puts the result back into the stack. The expression ends, and there is one number left in the stack — 1, which is the result of the calculation.

### Input Format

A single line is entered containing space-separated integers and operators +, -, *, which together form a valid expression in Reverse Polish Notation.

### Output Format:

A single integer is output — the result of the expression's calculation.

### Example 1

__Input__
```plaintext
7 2 3 * -
```

__Output__
```plaintext
1
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
2 5 - -2 -
```

__Output__
```plaintext
-1
```