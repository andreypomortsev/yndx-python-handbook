## [File Difference](../../../solutions/3.5/35_h.py)

Write a program that determines which words appear in only one of the files.

### Input Format

The user inputs three filenames.\
Each input file contains an arbitrary number of words separated by spaces and newline characters.

### Output Format:

In the third file, output a list of words that appear in only one of the files, in alphabetical order without repetitions.

### Example

__Input__
```plaintext
# User input:
first.txt
second.txt
answer.txt

# Content of first.txt
кофе молоко
чай печенье
велосипед

# Content of second.txt
кофе велосипед
пряник жвачка весло
```

__Output__
```plaintext
# Content of answer.txt
весло
жвачка
молоко
печенье
пряник
чай
```