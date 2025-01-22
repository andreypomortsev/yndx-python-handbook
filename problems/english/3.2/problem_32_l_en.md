## [Namesakes — 2](../../../solutions/3.2/32_l.py)

Again, we help the HR employee determine how many male namesakes work in the organization, but now under slightly different conditions.

### Input Format

The first line specifies the number of men — employees of the organization ($N$).\
The next $N$ lines contain the last names of these employees in arbitrary order.

### Output Format:

A list of namesakes in the organization with their count, sorted in alphabetical order.\
If there are none, output "Однофамильцев нет".

### Example 1

__Input__
```plaintext
6
Иванов
Петров
Сидоров
Петров
Иванов
Петров
```

__Output__
```plaintext
Иванов - 2
Петров - 3
```

### Example 2

__Input__
```plaintext
3
Иванов
Петров
Сидоров
```

__Output__
```plaintext
Однофамильцев нет
```