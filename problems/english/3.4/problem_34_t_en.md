## [Truth Table 3](../../../solutions/3.4/34_t.py)

Let’s continue working with truth tables.\
Unfortunately, some Boolean algebra operations are not implemented in Python.\
The most common non-standard operations are: implication, exclusive disjunction, and equivalence.

We’ll denote them as follows:

- Implication — `->`;
- Exclusive disjunction — `^`;
- Equivalence — `~`.

Write a program that builds the truth table for a given complex logical expression.

### Input format

A logical expression involving several variables.

Possible content of the expression:

- Uppercase Latin letter — variable;
- `not` — negation;
- `and` — conjunction;
- `or` — disjunction;
- `^` — exclusive disjunction;
- `->` — implication;
- `~` — equivalence;
- `()` — logical parentheses.

### Output format:

Print the truth table for the given expression.

### Notes (from Yandex)

Before implementing the new operations, pay attention to their precedence.
It is recommended to use the knowledge gained in the "Polish calculator" task.

### Notes (from Me)

You need to clean the input data, as there may be cases like this in the test:

```plaintext
A -> B ~C
```

For solving this task, it is better to [convert from infix notation to postfix notation](https://www.youtube.com/live/km0E_i8Dtso?si=tnpIrI4mPoAVW1RG&t=1581).

### Example 1

__Input__
```plaintext
A -> B ~ C
```

__Output__
```plaintext
A B C F
0 0 0 0
0 0 1 1
0 1 0 0
0 1 1 1
1 0 0 1
1 0 1 0
1 1 0 0
1 1 1 1
```

### Example 2

__Input__
```plaintext
A or C ~ not (A -> B) or C
```

__Output__
```plaintext
A B C F
0 0 0 1
0 0 1 1
0 1 0 1
0 1 1 1
1 0 0 1
1 0 1 1
1 1 0 0
1 1 1 1
```