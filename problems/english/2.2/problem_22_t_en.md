## [Bunny — 2](../../../solutions/2.2/22_t.py)

On the way home, the parents decided to play a game with the children called "find the animals."

### Input Format

Three lines describing the roadside area.

### Output Format:

A string that contains the word "зайка" followed by its length.  
If there are multiple such strings, choose the one that is lexicographically smallest.

### Example 1

**Input**
```plaintext
березка елочка зайка волк березка
сосна сосна сосна елочка грибочки медведь
сосна сосна сосна белочка сосна белочка
```

**Output**
```plaintext
березка елочка зайка волк березка 33
```

### Example 2

**Input**
```plaintext
зайка березка
березка зайка
березка елочка березка
```

**Output**
```plaintext
березка зайка 13
```

## Solution

There are several approaches to solving this task, but they are the same in terms of [asymptotic complexity](https://en.wikipedia.org/wiki/Asymptotic_analysis). I like the approach of sorting the strings using permutation and then searching for the key word from the smaller string to the larger one. In the worst case, there will be sorting and two searches through the strings.
