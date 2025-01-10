## [Maximum Sum](../../../solutions/2.4/24_h.py)

The kids in kindergarten are playing with numbers again. Although they don't know numbers very well, they love inventing them.  
They decided that they would take turns calling out numbers, and whoever calls out the number with the highest sum of digits would be considered the winner.  
They chose the poor teacher as the judge and asked us for help. Write a program that will determine the winner.

### Input Format

The first line contains a number $N$ — the number of children in the group. Then the name of each child and their number are provided (each on a separate line).

### Output Format

You need to output the name of the winner. If two children called out numbers with the same sum of digits, the one who went last is considered the winner.

### Example 1

**Input**
```plaintext
2
Аня
123
Боря
234
```

**Output**
```plaintext
Боря
```

### Example 2

**Input**
```plaintext
3
Аня
1234
Боря
234
Ваня
2323
```

**Output**
```plaintext
Ваня
```