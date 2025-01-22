## [Bunny - 7](../../../solutions/3.1/31_h.py)

Once again, let's search for bunnies outside the train window.

### Input format

The first line contains a natural number $N$ — the number of designated roadside areas.  
Each of the following $N$ lines contains a description of a roadside area.

### Output format

For each line, find the position of the first bunny.  
If there are no bunnies in the line, this must be reported.

### Note

Use 1-based indexing for the characters in the strings.

### Example 1

__Input__
```plaintext
3
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка
```

__Output__
```plaintext
16
7
Заек нет =(
```

### Example 2

__Input__
```plaintext
4
зайка березка
березка зайка
березка елочка березка
елочка елочка елочка
```

__Output__
```plaintext
1
9
Заек нет =(
Заек нет =(
```