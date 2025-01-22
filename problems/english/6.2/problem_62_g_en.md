## [Failure Report](../../../solutions/6.2/62_g.py)

We will continue processing the DataFrame from the previous task.

Write a function `need_to_work_better`, which selects those who have at least one failing grade.

### Note

Your solution should contain only functions.\
The required functions should not be called within the solution.

### Example

__Input__
```python
columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)
```

__Output__
```plaintext
       name  maths  physics  computer science
0    Иванов      5        4                 5
1    Петров      4        4                 2
2   Сидоров      5        4                 5
3  Васечкин      2        5                 4
4  Николаев      4        5                 3
       name  maths  physics  computer science
1    Петров      4        4                 2
3  Васечкин      2        5                 4
```