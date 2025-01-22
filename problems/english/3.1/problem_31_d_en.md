## [Data Cleaning](../../../solutions/3.1/31_d.py)

The local provider collects a large number of logs, but often the report files become corrupted.  
The most common issues are errors like ## and @@@.  
Write a program that removes:

- Two # characters at the beginning of informational messages;
- Lines that end with three @ symbols.

### Input format

Report lines are entered. An empty line marks the end of input.

### Output format

Cleaned data.

### Example 1

__Input__
```plaintext
Hello, world
Hello, @@@
##Goodbye
```

__Output__
```plaintext
Hello, world
Goodbye
```

### Example 2

__Input__
```plaintext
First Message
##Second Message
@@@Third Message##
##Fourth Message@@@
```

__Output__
```plaintext
First Message
Second Message
@@@Third Message##
```