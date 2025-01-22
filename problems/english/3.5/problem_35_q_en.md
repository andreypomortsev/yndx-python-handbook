## [Hide and Seek](../../../solutions/3.5/35_q.py)

Steganography is a way of transmitting or storing information while keeping the very fact of such transmission (or storage) secret.

Unlike cryptography, which hides the content of a secret message, steganography hides the very fact that a message exists. Typically, the message will look like something else, such as an image, an article, a shopping list, a letter, or a Sudoku puzzle. Steganography is usually used in conjunction with cryptography, thus complementing it.

We were given a file with hidden text. It was mentioned that to extract the useful information, we need to "extract" the least significant byte from each character code in the text. This will be the character code of the useful information.
However, there is one "catch." If the character code is less than 128, it is the useful information.

Develop a program that extracts the useful information from the text file.

### Input format

The text is stored in the file _secret.txt_.

### Output format:

Output the hidden message.

### Example

__Input__
```plaintext
᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!
```

__Output__
```plaintext
Hello, world!
```