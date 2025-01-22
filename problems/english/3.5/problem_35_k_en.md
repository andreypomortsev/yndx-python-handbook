## [File Statistics 2.0](../../../solutions/3.5/35_k.py)

Write a program that calculates the following parameters for a given file:

- the total number of numbers;
- the number of positive numbers;
- the minimum number;
- the maximum number;
- the sum of all numbers;
- the arithmetic mean of all numbers rounded to two decimal places.

### Input format

The user enters two file names.\
The first file contains an arbitrary number of numbers separated by spaces and newline characters.

### Output format:

Output the statistics to the second file in _JSON_ format.

Set the keys of the values as follows:

- _count_ — the total number of numbers;
- _positive_count_ — the number of positive numbers;
- _min_ — the minimum number;
- _max_ — the maximum number;
- _sum_ — the sum of all numbers;
- _average_ — the arithmetic mean of all numbers rounded to two decimal places.

### Example

__Input__
```plaintext
# User input:
numbers.txt
statistics.json

# Contents of the numbers.txt file
1 2 3 4 5
-5 -4 -3 -2 -1
10 20
20 10
```

__Output__
```plaintext
# Contents of the statistics.json file
{
    "count": 14,
    "positive_count": 9,
    "min": -5,
    "max": 20,
    "sum": 60,
    "average": 4.29
}
```