## [Announce the List](../../../solutions/3.3/33_j.py)

Sometimes, when analyzing text, it's important to be able to identify words with certain characteristics — for example, by the number of vowels.
In this problem, we'll practice exactly this kind of filtering: you will look for words that contain at least three vowels, regardless of language or case.

You are given a string `words`.
Write an expression that creates a list of words that contain at least three vowels (in any case).

### Note

There should be nothing in your solution except an expression.

In Russian, the vowels are: $аяуюоёэеиы$

In English: $aeiouy$

<details>
<summary><h4>Hint</h4></summary>

Compose a basic expression:

```python
[word for word in words.split() if exp]
```

For exp, we recommend writing an expression like:

```python
sum(... for letter in word if ...) >= 3
```

</details>

### Example 1

__Input__
```plaintext
words = 'Ехали медведи на велосипеде'
```

__Output__
```plaintext
['Ехали', 'медведи', 'велосипеде']
```

### Example 2

__Input__
```plaintext
words = 'My homework is too difficult!'
```

__Output__
```plaintext
['homework', 'difficult!']
```
