## [Redesign of Multiplication Table](../../../solutions/2.4/24_p.py)

Agree that the previous multiplication tables don't look very nice. Let's set the same width for all columns and center the values within the cells.  
And yes, the client also asked to add borders between the cells.

### Input format

The first line contains the required **size** of the table. The second line contains the **width** of the columns.

### Output format:

A multiplication table of the specified size and appearance.

### Example 1

__Input__
```plaintext
3
3
```

__Output__
```plaintext
 1 | 2 | 3 
-----------
 2 | 4 | 6 
-----------
 3 | 6 | 9 
```

### Example 2

__Input__
```plaintext
5
5
```

__Output__
```plaintext
  1  |  2  |  3  |  4  |  5  
-----------------------------
  2  |  4  |  6  |  8  | 10  
-----------------------------
  3  |  6  |  9  | 12  | 15  
-----------------------------
  4  |  8  | 12  | 16  | 20  
-----------------------------
  5  | 10  | 15  | 20  | 25  
```