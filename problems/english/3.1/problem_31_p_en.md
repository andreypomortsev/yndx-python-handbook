## [News Announcement 2.0](../../../solutions/3.1/31_p.py)

Let's try again to shorten the headlines for articles in the news feed of a news website. Let's create a program that shortens a long headline to the required length and adds an ellipsis "..." if necessary.

### Input Format

A natural number $L$ is entered — the required length of the headline.\
A natural number $N$ is entered — the number of lines in the news headline.\
Each of the next $N$ lines contains one line of the headline.

### Output Format:

The shortened headline.

### Notes

The ellipsis counts towards the headline length.\
The newline character is not considered when calculating the length.

### Example 1

__Input__
```plaintext
144
5
Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
Благодаря ей он может регулировать громкость,
показывая расстояние между большим и указательным пальцами.
Для этого ему понадобилась веб-камера, знания Python и
библиотека для работы с компьютерным зрением.
```

__Output__
```plaintext
Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
Благодаря ей он может регулировать громкость...
```

### Example 2

__Input__
```plaintext
121
5
Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
Благодаря ей он может регулировать громкость,
показывая расстояние между большим и указательным пальцами.
Для этого ему понадобилась веб-камера, знания Python и
библиотека для работы с компьютерным зрением.
```

__Output__
```plaintext
Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана
Благодаря ей он может...
```