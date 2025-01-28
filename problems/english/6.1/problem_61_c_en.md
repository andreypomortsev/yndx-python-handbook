## [Any Options?](../../../solutions/6.1/61_c.py)

Vasya came to an educational seminar and discovered that there are $N$ attendees and $M$ seats.\
Help Vasya determine the probability that he will get a seat at the seminar.

### Input format

Two numbers $N$ and $M$.

### Output format

Two numbers — the number of favorable outcomes where Vasya gets a seat and the total number of possible group arrangements for the seminar.

### Note

In the first example, let's label the participants with the numbers 1, 2, 3, 4. Suppose 1 is Vasya.

Then all the variations of participants look like this:

- 1 2
- 1 3
- 1 4
- 2 3
- 2 4
- 3 4

The favorable outcomes for Vasya are only 3:

- 1 2
- 1 3
- 1 4

### Example 1

__Input__
```plaintext
4 2
```

__Output__
```plaintext
3 6
```

### Example 2

__Input__
```plaintext
10 3
```

__Output__
```plaintext
36 120
```