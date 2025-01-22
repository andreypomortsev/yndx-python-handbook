## [Progress Report](../../../solutions/6.2/62_f.py)

All educational institutions maintain performance journals. This is a great example of data that needs to be processed.

Consider the journal of a summer olympiad school, where the main subjects are mathematics, physics, and computer science. The performance data is presented as a _DataFrame_ with the following columns:

- `name` — name;
- `maths` — grade in mathematics;
- `physics` — grade in physics;
- `computer science` — grade in computer science.

Write a function `best` that filters all "high achievers" in the journal.

### Note

Your solution should contain only functions.\
There should be no calls to the required functions in the solution.

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
filtered = best(journal)
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
0   Иванов      5        4                 5
2  Сидоров      5        4                 5
```

## Solution Approach

To filter the _DataFrame_ with the condition that all grades of the student (rows) must be greater than 3, we use boolean masks.

### Solution Steps

__1. Exclude the name column for comparison__

   Since we only need to compare numerical data (grades), we remove the `name` column using `pd.DataFrame.iloc[:, 1:]`. This leaves only the grades:

   ```plaintext
      maths  physics  computer science
   0      5        4                 5
   1      4        4                 2
   2      5        4                 5
   3      2        5                 4
   4      4        5                 3
   ```

__2. Create a boolean mask based on the condition__

   We compare all elements with the number 3 using `(journal.iloc[:, 1:] > 3)`. This creates a mask where each value indicates whether the condition is satisfied for the corresponding grade:

   ```plaintext
      maths  physics  computer science
   0   True     True              True
   1   True     True             False
   2   True     True              True
   3  False     True              True
   4   True     True             False
   ```

__3. Identify rows that satisfy the condition__

   To keep only those rows where all values are `True`, we use the `.all(axis=1)` method.  
   The `axis=1` parameter indicates that the check should be performed across rows (for each student). The result will be a series of boolean values indicating which rows should be kept:

   ```plaintext
   0     True
   1    False
   2     True
   3    False
   4    False
   dtype: bool
   ```

   If we omit the `axis=1` parameter (which defaults to `axis=0`), the check will be performed across columns, and the result will be:

   ```plaintext
   maths               False
   physics              True
   computer science    False
   dtype: bool
   ```

   This result is not suitable for our task.

__4. Filter the data using the mask__

   We apply the obtained boolean mask to the original _DataFrame_ to keep only the rows that satisfy the condition:

   ```python
   journal[(journal.iloc[:, 1:] > 3).all(axis=1)]
   ```

### Final Result
For the given example, the data is filtered as follows:

__Original DataFrame:__

```plaintext
       name  maths  physics  computer science
0    Иванов      5        4                 5
1    Петров      4        4                 2
2   Сидоров      5        4                 5
3  Васечкин      2        5                 4
4  Николаев      4        5                 3
```

__Filtered DataFrame:__

```plaintext
      name  maths  physics  computer science
0   Иванов      5        4                 5
2  Сидоров      5        4                 5
```