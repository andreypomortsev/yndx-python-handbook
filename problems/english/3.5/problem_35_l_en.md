## [Divide and Conquer](../../../solutions/3.5/35_l.py)

Write a utility that divides the numbers in a file into three groups:

- numbers with a predominance of even digits;
- numbers with a predominance of odd digits;
- numbers with an equal number of even and odd digits.

### Input format

The user enters four file names.\
The first file contains an arbitrary number of numbers separated by spaces and newline characters.

### Output format:

Output the numbers that meet the required condition into the other three files.\
Preserve the position of the numbers in the lines.

### Example

__Input__
```plaintext
# User input:
numbers.txt
even.txt
odd.txt
eq.txt

# Contents of the numbers.txt file
650975472 591084323 629700 1504180 577023
8460612246 42161437 29409368 58531725 5725268 2198001838
796451 69358 7195510 975628465 9756641
44200289 126541 979391 93479581 291170 28987042 86139603
```

__Output__
```plaintext
# Contents of the even.txt file
629700 1504180
8460612246 29409368 5725268 2198001838
975628465
44200289 28987042

# Contents of the odd.txt file
650975472 591084323 577023
58531725
796451 69358 7195510 9756641
979391 93479581 291170

# Contents of the eq.txt file

42161437

126541 86139603

```