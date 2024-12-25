## [First player, get ready](../../../solutions/2.2/22_i.py)

In many games, the order is determined by the toss of a die or a coin — and in our case, the first turn goes to the player whose name is lexicographically smaller.

Determine which player will go first.

### Input format

Three player names, each written on a new line.

### Output format:

The name of the player who will go first.

### Example 1

**Input**
```plaintext
Вова
Аня
Боря
```

**Output**
```plaintext
Аня
```

### Example 2

**Input**
```plaintext
Толя
Коля
Вася
```

**Output**
```plaintext
Вася
```

## Solution

We use the logic from problem [D](problem_22_d_ru.md), but here we only need two comparisons since we need to find the lexicographically smaller name.