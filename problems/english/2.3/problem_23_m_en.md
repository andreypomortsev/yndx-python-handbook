## [Player One, Prepare 2.0](../../../solutions/2.3/23_m.py)

In many games, the order of turns is determined by a dice roll or coin flip, but in our case, the player whose name is lexicographically smaller goes first. Determine which player will take the first turn.

### Input Format

The first line contains a single natural number $N$ — the number of players.
Each of the next $N$ lines contains one player's name.

### Output Format:

The name of the player who will go first.

### Example 1

__Input__
```plaintext
3
Вова
Аня
Боря
```

__Output__
```plaintext
Аня
```

### Example 2

__Input__
```plaintext
4
Толя
Коля
Вася
Юля
```

__Output__
```plaintext
Вася
```