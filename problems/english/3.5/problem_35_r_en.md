## [How Much Does it Weigh in Bytes?](../../../solutions/3.5/35_r.py)

Size is an important characteristic of any file. According to GOST 8.417-2002 in our country, the volume of information is measured in the following units:

| Size          | English  | Russian   |
|---------------|----------|-----------|
| bit           | b        | б   |
| Byte          | B        | Б  |
| Kilobyte      | KB       | КБ |
| Megabyte      | MB       | МБ |
| Gigabyte      | GB       | ГБ |

Write a program that calculates the size of a given file and returns the size in the corresponding Russian units of measurement.

### Input format

The program will receive a file name.

### Output format:

Output the size of the file in the appropriate units of measurement. If the result is a fractional value, round it up.

### Note

To solve this task, you can choose one of the following approaches:

- Study file reading in byte mode.
- Use the standard library [os](https://docs.python.org/3/library/os.path.html#os.path.getsize).

### Example 1

__Input__
```plaintext
file.txt
```

__Contents of file.txt__
```plaintext
This file weighs more than it seems ))
```

__Output__
```plaintext
67B
```

### Example 2

__Input__
```plaintext
another_file.txt
```

__Contents of another_file.txt__
```plaintext
I would like to make an example with a file larger than 1KB
Don't worry, such a file will definitely appear in hidden tests ))
```

__Output__
```plaintext
193B
```