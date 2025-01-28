## [Porridge Eaters](../../../solutions/3.2/32_d.py)

Each kindergarten child likes either semolina porridge, oatmeal porridge, or both.  
Let's create a program that will allow the caregiver to quickly find out how many children like both types of porridge.

### Input Format

The first two lines indicate the number of children who like semolina and oatmeal porridge ($N$ and $M$).  
Then follow $N$ lines with the names of children who like semolina porridge, and $M$ lines with the names of children who like oatmeal porridge.  
It is guaranteed that there are no children with the same last name in the group.

### Output Format:

The number of children who like both types of porridge.  
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
Таких нет
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
3
```