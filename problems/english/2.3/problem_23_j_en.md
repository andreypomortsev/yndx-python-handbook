## [Route Built](../../../solutions/2.3/23_j.py)

Navigation has always been important.
We have received an archive of routes, but there are so many of them that without automation, we won't be able to handle them. Each route consists of a sequence of steps in one of four directions:

- NORTH (СЕВЕР in rus);
- EAST (ВОСТОК in rus);
- SOUTH (ЮГ in rus);
- WEST (ЗАПАД in rus).

Write a program that, given a route, determines the exact point where we will end up.
For simplicity, let's assume that at the start of the route, we are at point (0; 0).

### Input Format

Route instructions are entered as:

\<direction>\
\<number of steps>

The input ends with the string STOP.

### Output Format:

Two integers — the coordinates of the final point of the route.

### Example 1

**Input**
```plaintext
СЕВЕР
2
ВОСТОК
2
СТОП
```

**Output**
```plaintext
2
2
```

### Example 2

**Input**
```plaintext
СЕВЕР
2
ЮГ
3
ЗАПАД
4
СТОП
```

**Output**
```plaintext
-1
-4
```