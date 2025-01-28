## [Game Grid](../../../solutions/3.4/34_g.py)

The kids in the class decided to organize a checkers tournament. Unfortunately, the number of students is not a power of two, so it is difficult to create a classic tournament bracket. To identify the favorites, the kids agreed to play a "round-robin" format. Think of a program that generates a list of the necessary games.

### Input format

The first line contains the number of students ($N$).\
Each of the following $N$ lines contains one name.

### Output format:

A list of games in the format:\
_<Player 1> - <Player 2>_\
The order of the games doesn't matter.

### Example

__Input__
```plaintext
3
Аня
Боря
Вова
```

__Output__
```plaintext
Аня - Боря
Аня - Вова
Боря - Вова
```