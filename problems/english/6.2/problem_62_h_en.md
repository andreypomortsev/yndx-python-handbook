## [Gradebook Update](../../../solutions/6.2/62_h.py)

We will continue processing the _DataFrame_ from the previous tasks.

Write a function `update`, which adds a column `average` containing the average grade for each student, and sorts the data by descending average grades, and lexicographically by name if the averages are equal.

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
filtered = update(journal)
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
       name  maths  physics  computer science   average
0    Иванов      5        4                 5  4.666667
2   Сидоров      5        4                 5  4.666667
4  Николаев      4        5                 3  4.000000
3  Васечкин      2        5                 4  3.666667
1    Петров      4        4                 2  3.333333
```