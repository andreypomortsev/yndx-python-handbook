## [Binary Statistics!](../../../solutions/3.2/32_o.py)

Programmers have a special relationship with the binary number system.\
Let’s continue practicing data processing and analyze the given numbers.\
Write a program that calculates for the provided numbers:

- the number of digits;
- the number of ones;
- the number of zeros.

### Input Format

A sequence of numbers separated by spaces.

### Output Format:

Output a list of dictionaries containing the required statistics.

### Note

The output in the examples is formatted solely for visual clarity.\
All whitespace characters should be ignored during validation.\
The order of dictionaries must match the order of the provided numbers.\
The order of the keys in the dictionary does not matter.

### Example 1

__Input__
```plaintext
5 8 12
```

__Output__
```plaintext
[
    {
        "digits": 3,
        "units": 2,
        "zeros": 1
    },
    {
        "digits": 4,
        "units": 1,
        "zeros": 3
    },
    {
        "digits": 4,
        "units": 2,
        "zeros": 2
    }
]
```

### Example 2

__Input__
```plaintext
13 2 7
```

__Output__
```plaintext
[
    {
        "digits": 4,
        "units": 3,
        "zeros": 1
    },
    {
        "digits": 2,
        "units": 1,
        "zeros": 1
    },
    {
        "digits": 3,
        "units": 3,
        "zeros": 0
    }
]
```