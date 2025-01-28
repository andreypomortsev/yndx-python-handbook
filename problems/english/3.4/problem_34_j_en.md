## [We Divided the Orange 2.0](../../../solutions/3.4/34_j.py)

Anya, Borja, and Vova decided to eat an orange.\
Tell the kids how they can divide it.

Develop a program that prints all possible ways of dividing the orange.

### Input format

A single line contains the number of orange slices ($N$).

### Output format:

A table of division options.

### Notes

- Each child must get at least one slice of the orange.
- No slice should remain.
- Print the options in order of increasing slices for Anya, then Borja, and then Vova.\
For convenience, reduce the problem to dividing the slices between two people, and give the remainder to the third.

### Example 1

__Input__
```plaintext
3
```

__Output__
```plaintext
А Б В
1 1 1
```

### Example 2

__Input__
```plaintext
5
```

__Output__
```plaintext
А Б В
1 1 3
1 2 2
1 3 1
2 1 2
2 2 1
3 1 1
```