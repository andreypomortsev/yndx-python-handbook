## [Bunny — 10](../../../solutions/3.2/32_p.py)

Let's help children figure out what exactly they saw near the hares.

### Input Format

Each line contains a description of the roadside landscape.\
The input ends with an empty line.

### Output Format:

Determine the list of things seen near the hares, without duplicates.\
The order of output does not matter.

### Note

An object is considered to be next to a hare if it is written immediately to the left or right of it.

### Example 1

__Input__
```plaintext
березка елочка зайка волк березка
сосна зайка сосна елочка зайка медведь
сосна сосна сосна белочка сосна белочка
```

__Output__
```plaintext
волк
елочка
медведь
сосна
```

### Example 2

__Input__
```plaintext
зайка березка
березка зайка
березка елочка березка
елочка елочка елочка
```

__Output__
```plaintext
березка
```