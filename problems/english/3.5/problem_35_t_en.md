## [File Sum](../../../solutions/3.5/35_t.py)

You are probably aware that there are not only text files. Various data formats involve special encoding. For example, _BMP_ images store some header information and the colors of all pixels as numbers.

Let's work with such data. We are given a file in some format, let's call it _NUM_. It contains a list of 2-byte numbers. For simplicity, we will assume that there are no negative numbers.

Write a program that computes the sum of all the numbers in the file within the 2-byte range.

### Input Format

The file _numbers.num_ contains numbers in the specified format.

### Output Format:

One number — the sum of all the numbers in the file within the 2-byte range.

### Note

For simplicity, the files in the examples are recorded in _HEX_ format. In this form, the file appears as a sequence of four-digit hexadecimal numbers.

In the first example, five hexadecimal numbers are recorded: 1, 2, 3, 4, 5. Their sum is 15.
In the second example, 255 and 257 are recorded. Their sum is 512.

You can download the example files in their original form here:

- [First Example](https://yastatic.net/s3/ml-handbook/admin/sample01_10c35fbe0c.num?updated_at=2022-10-19T08:17:14.880Z)
- [Second Example](https://yastatic.net/s3/ml-handbook/admin/sample02_040e003db4.num?updated_at=2022-10-19T08:17:32.254Z)

If you want to learn about how integers are stored in computers, we recommend reading about direct, inverse, and two's complement representations.

### Example 1

__Input__
```plaintext
0001 0002 0003 0004 0005
```

__Output__
```plaintext
15
```

### Example 2

__Input__
```plaintext
00FF 0101
```

__Output__
```plaintext
512
```