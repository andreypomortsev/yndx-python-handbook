## [Simple Task 4.0](../../../solutions/3.2/32_t.py)

Let's recall that two numbers are said to be coprime if they don't share any divisors other than 1. Write a program that, for each given number, finds a list of its coprimes among the provided numbers.

### Input format

A sequence of numbers is given, separated by semicolons (`;`) and spaces.

### Output format:

A list of numbers with their coprimes among the provided numbers.  
All numbers should be printed in ascending order, without duplicates.  
The output should be formatted as follows:  
_number - coprime 1, coprime 2, ..._  
If a number has no coprimes, it should not be printed.

### Example 1

__Input__
```plaintext
2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20
```

__Output__
```plaintext
2 - 3, 5, 7, 9, 11, 13, 15, 17, 19
3 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20
4 - 3, 5, 7, 9, 11, 13, 15, 17, 19
5 - 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19
6 - 5, 7, 11, 13, 17, 19
7 - 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20
8 - 3, 5, 7, 9, 11, 13, 15, 17, 19
9 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20
10 - 3, 7, 9, 11, 13, 17, 19
11 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20
12 - 5, 7, 11, 13, 17, 19
13 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20
14 - 3, 5, 9, 11, 13, 15, 17, 19
15 - 2, 4, 7, 8, 11, 13, 14, 16, 17, 19
16 - 3, 5, 7, 9, 11, 13, 15, 17, 19
17 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20
18 - 5, 7, 11, 13, 17, 19
19 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20
20 - 3, 7, 9, 11, 13, 17, 19
```

### Example 2

__Input__
```plaintext
7; 2; 2; 12; 14; 7; 2; 49
```

__Output__
```plaintext
2 - 7, 49
7 - 2, 12
12 - 7, 49
49 - 2, 12
```