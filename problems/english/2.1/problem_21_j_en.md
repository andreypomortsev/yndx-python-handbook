## [Kindergarten — Overalls](../../../solutions/2.1/21_j.py)

Continuing the kindergarten theme, let's automate something there as well.  
Each child has an assigned locker and bed. The locker number consists of three digits:

- The group number in the kindergarten;
- The number of the bed assigned to the child;
- The child's sequential number in the group list.

The teacher asks to create a program that, given the child's name and their locker number, generates a "beautiful" card for their personal file.

### Input Format:

- The first line contains the child's name.  
- The second line contains the locker number.

### Output Format:

A card in the following format:

```plaintext
Группа №<номер группы>.  
<номер ребёнка в списке>. <имя ребенка>.  
Шкафчик: <номер шкафчика>.  
Кроватка: <номер кроватки>.
```

### Example 1

__Input__  
```plaintext
Ванечка
832
```

__Output__  
```plaintext
Группа №8.
2. Ванечка.
Шкафчик: 832.
Кроватка: 3.
```

### Example 2

__Input__  
```plaintext
Машенька
141
```

__Output__  
```plaintext
Группа №1.
1. Машенька.
Шкафчик: 141.
Кроватка: 4.
```