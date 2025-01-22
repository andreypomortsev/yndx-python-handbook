## [Are there any other options?](../../../solutions/3.4/34_q.py)

Let's help Vitaly once again figure out which variations of drawing certain triples of cards from the deck are possible. Write a program that outputs a list of variations according to the requirements.

### Input format

The first line contains the suit that must be present in the triple. The second line contains the rank that must not be in the triple. The third line contains the previous variation obtained by Vitaly.

### Output format:

Print the next variation of the layout.

### Note

Note: the jack-queen-king-ace are lexicographically ordered. But "10 ..." is lexicographically less than "2 ...", and diamonds are less than spades.

Suits in the nominative and genitive cases:
| Nominative | Genitive  |
|------------|-----------|
| буби       | бубен     |
| пики       | пик       |
| трефы      | треф      |
| черви      | червей    |

### Example 1

__Input__
```plaintext
spades
10
9 пик, король треф, туз червей
```

__Output__
```plaintext
9 пик, король червей, туз бубен
```

### Example 2

__Input__
```plaintext
трефы
король
2 червей, туз пик, туз треф
```

__Output__
```plaintext
2 червей, туз треф, туз червей
```