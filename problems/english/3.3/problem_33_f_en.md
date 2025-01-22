## [Letter Frequency Statistics](../../../solutions/3.3/33_f.py)

You will be given a string `text`.

Write an expression to generate a dictionary that contains information about the frequency of letters in the given string.

When analyzing, ignore case, and use the lowercase letters that appear in the string as keys of the dictionary.

### Note

There should be nothing in the solution except the expression.

### Example 1

__Input__
```plaintext
text = 'Мама мыла раму!'
```

__Output__
```plaintext
{'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}
```

### Example 2

__Input__
```plaintext
text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
```

__Output__
```plaintext
{   
    'а': 6,
    'в': 2,
    'д': 5,
    'е': 7,
    'з': 2,
    'и': 5,
    'к': 1,
    'л': 2,
    'м': 3,
    'н': 3,
    'о': 3,
    'п': 2,
    'р': 1,
    'с': 1,
    'т': 1,
    'х': 1,
    'ё': 1
}
```