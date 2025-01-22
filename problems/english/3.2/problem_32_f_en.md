## [Porridge eaters — 3](../../../solutions/3.2/32_f.py)

Let's return to the condition where each child in kindergarten likes either semolina, oatmeal, or both types of porridge.  
Write a program that will allow the teacher to find out which children like only one type of porridge.

### Input Format

The first two lines indicate the number of children who like semolina and oatmeal porridge ($N$ and $M$).  
Then follow $N + M$ lines — shuffled last names of children.  
It is guaranteed that there are no children with the same last name in the group.

### Output Format:

In alphabetical order, print the last names of children who like only one type of porridge.  
If there are none, the output should be "Таких нет" (None).

### Example 1

__Input__
```plaintext
3
2
Васильев
Петров
Васечкин
Иванов
Михайлов
```

__Output__
```plaintext
Васечкин
Васильев
Иванов
Михайлов
Петров
```

### Example 2

__Input__
```plaintext
3
3
Иванов
Петров
Васечкин
Иванов
Петров
Васечкин
```

__Output__
```plaintext
Таких нет
```