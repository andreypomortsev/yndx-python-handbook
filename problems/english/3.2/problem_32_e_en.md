## [Porridge eaters — 2](../../../solutions/3.2/32_e.py)

Let's modify the task and write a program that will help quickly find out how many children like only one type of porridge.

### Input Format

The first two lines indicate the number of children who like semolina and oatmeal porridge ($N$ and $M$).  
Then follow $N + M$ lines — **shuffled last names** of children.  
It is guaranteed that there are no children with the same last name in the group.

### Output Format:

The number of children who like only one type of porridge.  
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
5
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