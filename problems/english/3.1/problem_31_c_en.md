## [News Announcement](../../../solutions/3.1/31_c.py)

A local news company ordered a website. An integral part of it is a news feed.  
To help users analyze articles more quickly, it is necessary to shorten headlines. Write a program that shortens long headlines to the required length and adds an ellipsis ... if necessary.

### Input format

A natural number $L$ is entered — the required length of the headline.  
A natural number $N$ is entered — the number of headlines that need to be shortened.  
Each of the following $N$ lines contains one headline.

### Output format

Shortened headlines.

### Note

The ellipsis is counted as part of the headline length.

### Example

__Input__
```plaintext
25
3
Начался саммит по глобальному потеплению
Завтра Новый год!
Python и Java конкурируют за звание самого популярного языка программирования
```

__Output__
```plaintext
Начался саммит по глоб...
Завтра Новый год!
Python и Java конкурир...
```