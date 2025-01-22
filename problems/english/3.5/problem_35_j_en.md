## [Tail](../../../solutions/3.5/35_j.py)

In Linux family operating systems, there's a useful command-line utility called `tail`. It's used when we don't need to read the entire file, but just want to view a few of the last lines.

Write an equivalent of this utility.

### Input Format

The user inputs the filename ($F$), followed by the number of lines ($N$) they want to see.

### Output Format:

Print the last $N$ lines of the file $F$.

### Example

__Input__
```plaintext
# User input:
some_file.txt
2

# Content of some_file.txt
1 строка
2 строка
3 строка
4 строка
5 строка
```

__Output__
```plaintext
4 строка
5 строка
```

## Approach

### Opening the file and moving the pointer

   - The file is opened in binary mode (`rb`) to work with bytes. This allows us to read the file line by line regardless of its encoding.
   - We use [`file.seek(0, 2)`](https://docs.python.org/3/library/io.html#io.IOBase.seek) to move the pointer to the end of the file.
   - Using `tell()`, which returns the size of the file in bytes, allows us to correctly manage pointer movement.

### Reading the file from the end

   - We use a buffer [`buffer`](https://docs.python.org/3.1/library/functions.html#bytearray) to progressively collect lines in binary form from the end of the file.
   - The loop continues until:
     1. The pointer reaches the beginning of the file `pointer_location > 0`.
     2. Enough lines are collected (lines are checked via the length of the `lines` array).
   - In each iteration:
        - The block size to read is either the remaining bytes to the start of the file or `SIZE` (32 bytes).
        - The pointer moves `chunk_size` bytes back: `file.seek(pointer_location - chunk_size)` towards the start of the file.
        - A chunk of data is read: `file.read(chunk_size)`.
        - The new data block is added to the beginning of the buffer: `buffer = chunk + buffer`, which is crucial, as opposed to `buffer += chunk`.
        - The buffer content is split by newline characters `\n`: `lines = buffer.split(b"\n")`.

### Checking the number of lines

   - The line counter is updated on each iteration: `read_lines = len(lines)`.
   - If the number of lines (`read_lines`) becomes greater than or equal to `tail + 1`, reading stops. This prevents unnecessary file reading.

### Output the last lines

   - The last `tail` lines are selected from the `lines` array: `lines[-tail:]`, because when reading in chunks, we might read some extra "partial" lines.
   - Each line is decoded from bytes to a string with the specified encoding (`DEFAULT_ENCODING`) and printed.