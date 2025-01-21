## [Just hello, just how are you.](../../../solutions/2.2/22_a.py)

A conversation skill is an important trait for a polite person.

Write a dialogue program that first introduces itself to the user and then inquires about their mood.

### Input format

The first line contains the user's name.
The second line contains the answer to the question: "хорошо" or "плохо".

### Output format:

The first line should be the question "Как Вас зовут?"
The second line should be "Здравствуйте, %username%!"
The third line should be the question "Как дела?"
The fourth line should be the response to the user's answer:

- If the user answers "хорошо", the message "Я за вас рада!" should be displayed;
- If the user answers "плохо", the message "Всё наладится!" should be displayed.

### Example 1

__Input__
```plaintext
Аня
хорошо
```

__Output__
```plaintext
Как Вас зовут?
Здравствуйте, Аня!
Как дела?
Я за вас рада!
```

### Example 2

__Input__
```plaintext
Боря
плохо
```

__Output__
```plaintext
Как Вас зовут?
Здравствуйте, Боря!
Как дела?
Всё наладится!
```