## [Generalization](../../../solutions/3.3/33_t.py)

Congratulations, this is the last problem in the set!
Let's finish on a high note — now you'll combine everything you've learned about sets, list comprehensions, and data filtering.

In this task, you will analyze a text and determine pairs of words that have at least three letters in common.
Important: the order of words in a pair does not matter, and repeated letters are only counted once.

You are given a variable `text`.

Write an expression to generate a set containing all tuples of word pairs that have more than two letters in common (ignoring repetitions).
Pairs with different word orders should be considered the same and included in the result only once (in lexicographically sorted order).

### Note

There should be nothing in your solution except an expression.

All words in the text are unique.

<details>
<summary><h4>Hint</h4></summary>

1. Use nested loops in a list comprehension to iterate over all pairs
2. For filtering, convert words to sets and find their intersection
3. Sort the words in the tuples to avoid duplicates

</details>

### Example 1

__Input__
```plaintext
text = 'ехали медведи на велосипеде'
```

__Output__
```plaintext
{('велосипеде', 'медведи'), ('велосипеде', 'ехали')}
```

### Example 2

__Input__
```plaintext
text = 'а за ними кот задом наперед'
```

__Output__
```plaintext
set()
```
