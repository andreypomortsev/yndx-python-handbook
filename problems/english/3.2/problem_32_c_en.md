## [Bunny — 8](../../../solutions/3.2/32_c.py)

We continue counting hares outside the train window.

### Input Format

The first line contains a natural number $N$ — the number of identified roadside areas.  
Each of the following $N$ lines contains a description of a roadside area.

### Output Format:

Print all the found objects in the roadside areas.

### Example 1

__Input__
```plaintext
3
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка
```

__Output__
```plaintext
сосна
березка
волк
елочка
медведь
белочка
зайка
```

### Example 2

__Input__
```plaintext
4
зайка березка
березка зайка
березка елочка березка
елочка елочка елочка
```

__Output__
```plaintext
березка
елочка
зайка
```