## [The layout is as follows...](../../../solutions/3.4/34_p.py)

Vitaly loves playing cards. He decided to figure out which variations of drawing certain triples of cards from the deck exist. Write a program that outputs a list of variations according to the requirements.

### Input format

The first line contains the suit that must be present in the triple.\
The second line contains the rank that must not be in the triple.

### Output format:

Print the first 10 resulting triples on the screen.\
The cards in each combination must be sorted lexicographically (by the card name string). Cards in the combination are separated by a comma with a space after it.\
The combinations themselves must also be sorted lexicographically by the string representing the entire combination.

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
пики
10
```

__Output__
```plaintext
2 бубен, 2 пик, 2 треф
2 бубен, 2 пик, 2 червей
2 бубен, 2 пик, 3 бубен
2 бубен, 2 пик, 3 пик
2 бубен, 2 пик, 3 треф
2 бубен, 2 пик, 3 червей
2 бубен, 2 пик, 4 бубен
2 бубен, 2 пик, 4 пик
2 бубен, 2 пик, 4 треф
2 бубен, 2 пик, 4 червей
```

### Example 2

__Input__
```plaintext
трефы
король
```

__Output__
```plaintext
10 бубен, 10 пик, 10 треф
10 бубен, 10 пик, 2 треф
10 бубен, 10 пик, 3 треф
10 бубен, 10 пик, 4 треф
10 бубен, 10 пик, 5 треф
10 бубен, 10 пик, 6 треф
10 бубен, 10 пик, 7 треф
10 бубен, 10 пик, 8 треф
10 бубен, 10 пик, 9 треф
10 бубен, 10 пик, валет треф
```