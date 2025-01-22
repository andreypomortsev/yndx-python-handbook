## [File Cleaning](../../../solutions/3.5/35_i.py)

_Python_ is primarily a scripting language. Such languages are often used to create console utilities.

Write a simple utility that cleans the given file from:

- repeated spaces;
- repeated newline characters;
- tabs;
- excess spaces at the beginning and end of lines.

### Input Format

The user inputs two filenames.\
The input file contains unformatted text of arbitrary length.

### Output Format:

In the second file, output the cleaned text.

### Example

__Input__
```plaintext
# User input:
first.txt
second.txt

# Content of first.txt
    очень 		 плохо форматированный       текст


ну		ну	
прямо

очень-очень

	
```

__Output__
```plaintext
# Content of second.txt
очень плохо форматированный текст
нуну
прямо
очень-очень
```