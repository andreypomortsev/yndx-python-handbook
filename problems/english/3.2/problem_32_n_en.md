## [This will be a masterpiece!](../../../solutions/3.2/32_n.py)

The head cook of the kindergarten wants to quickly select dishes for cooking.\
He has a list of available ingredients and a set of dishes.

Write a program that can quickly determine which dishes can be cooked.

### Input Format

The number of ingredients ($N$) available.\
$N$ lines with ingredient names.\
The number of recipes ($M$) for which there is information.\
$M$ blocks of lines for each recipe.\
In the first line of each block, the name of the dish is given.\
In the second line, the number of ingredients.\
Then the ingredients required for the dish are listed.

### Output Format:

A list of dishes that can be cooked in alphabetical order.\
If no dishes can be prepared, output "Готовить нечего".

### Example 1

__Input__
```plaintext
4
Яблоки
Хлеб
Варенье
Картошка
3
Тосты
2
Хлеб
Варенье
Яблочный Сок
1
Яблоки
Яичница
1
Яйца
```

__Output__
```plaintext
Тосты
Яблочный Сок
```

### Example 2

__Input__
```plaintext
1
хлеб
1
бутерброд
2
масло
хлеб
```

__Output__
```plaintext
Готовить нечего
```