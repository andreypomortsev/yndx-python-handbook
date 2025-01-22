## [Everything will be found](../../../solutions/3.1/31_k.py)

Search functionality is one of the essential needs in the modern world. Let's build a small component for a search engine that checks if a search query appears in the page titles.

### Input format

A natural number $N$ is provided, representing the number of pages to search among.\
The next $N$ lines contain the page titles.\
The last line contains the search query.

### Output format

Output all the page titles that contain the search query (case insensitive).\
The order of the titles should be preserved.

### Example 1

__Input__
```plaintext
3
Google выпустил задачник по программированию
На соревнованиях по программированию победил любитель питона
Как заказать Google.Такси?!
Google
```

__Output__
```plaintext
Я выпустил задачник по программированию
Как заказать Google.Такси?!
```

### Example 2

__Input__
```plaintext
8
сериал шерлок смотреть онлайн
учебник питона
мемы
социальная сеть
упражнения по питону
кормовые мыши для питонов
ответы егэ скачать бесплатно
компьютерные мыши
питон
```

__Output__
```plaintext
учебник питона
упражнения по питону
кормовые мыши для питонов
```