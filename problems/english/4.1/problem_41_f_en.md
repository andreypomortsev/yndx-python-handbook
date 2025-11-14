## [Wierd Game](../../../solutions/4.1/41_f.py)

The first five tasks are already behind us — you are doing great!\
It's time to practice with mutable variables and decision-making logic.

Petya and Vanya decided to play the "Number Tug-of-War" game.
The rules are simple:

  - Petya (in input as 'Петя') increases the total number.
  - Vanya (in input as 'Ваня') decreases it.
  - If the result is a positive number, Petya wins.
  - If it's negative, Vanya wins.
  - If the sum is zero, it's a draw.

Create two functions:

  - `move(player, number)` — takes the player's name (in input as 'Петя' or 'Ваня') and their number, and updates the total score;
  - `game_over()` — returns the result: 'Petya', 'Vanya', or 'Draw'.
    The total sum is initially 0.

### Note

The solution should not contain calls to the required functions.

<details>
<summary>Hint</summary>
The task is similar to the previous one. Declare a global variable and modify it within the body of the first function.
</details>

### Example 1

__Input__

```python
move('Петя', 3)
move('Ваня', 4)
print(game_over())
```

__Output__

```plaintext
Ваня
```

### Example 2

__Input__

```python
move('Петя', 3)
move('Ваня', 4)
move('Петя', 4)
move('Ваня', 3)
print(game_over())
```

__Output__

```plaintext
Ничья
```