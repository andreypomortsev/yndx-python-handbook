## [Deck of cards](../../../solutions/3.4/34_f.py)

Generate and display a deck of playing cards without one of the suits: three suits from two to ace. The suit that should be removed is entered by the user. Use the `product` iterator to combine suits and ranks.

The card names should be in the format "rank suit". For example: «2 пик» ("2 of spades"), «10 треф» ("10 of clubs"), «валет бубен» ("jack of diamonds"), «дама червей» ("queen of hearts").\
The order of the suits matters.

### Input format

The name of the suit that should be removed is given in the same case as it will be displayed on the screen: «пик», «треф», «бубен» and «червей» ("spades", "clubs", "diamonds", and "hearts").

### Output format:

A list of cards in the deck, sorted by increasing rank, then suit (as in preference).

### Example

__Input__
```plaintext
треф
```

__Output__
```plaintext
2 пик
2 бубен
2 червей
3 пик
3 бубен
3 червей
4 пик
4 бубен
4 червей
5 пик
5 бубен
5 червей
6 пик
6 бубен
6 червей
7 пик
7 бубен
7 червей
8 пик
8 бубен
8 червей
9 пик
9 бубен
9 червей
10 пик
10 бубен
10 червей
валет пик
валет бубен
валет червей
дама пик
дама бубен
дама червей
король пик
король бубен
король червей
туз пик
туз бубен
туз червей
```