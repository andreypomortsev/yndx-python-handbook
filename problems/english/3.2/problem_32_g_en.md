## [Morse Code](../../../solutions/3.2/32_g.py)

You are given an English text. Encode it using the [Morse code](https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg). Each letter is replaced by a sequence of dots and dashes. Use a hyphen (-) for dashes and a period (.) for dots. For example, the letter 'g' will be encoded as `--..`. A single space should be placed between encoded letters. For instance, the word "Help" will be encoded as `.... . .-.. .--..`. Note that both lowercase and uppercase letters are encoded the same.

### Input Format

The entire text is given in a single line. The text consists of English letters and spaces, with no other characters. There are no consecutive spaces in the text.

### Output Format

Output each word from the original text encoded in Morse code on a separate line.  
The number of output lines should match the number of words in the input text.

### Note

A typical option for a Morse Code dictionary:

```copy
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
```


### Example 1

__Input__
```plaintext
Hello world
```

__Output__
```plaintext
.... . .-.. .-.. ---
.-- --- .-. .-.. -..
```

### Example 2

__Input__
```plaintext
Help me SOS
```

__Output__
```plaintext
.... . .-.. .--.
-- .
... --- ...
```