## [This Will Be Our Secret](../../../solutions/3.5/35_s.py)

The Caesar cipher, also known as the shift cipher, is one of the simplest and most widely known encryption methods. It is named after the Roman general Gaius Julius Caesar, who used it for secret correspondence with his generals.

Let's implement this encryption system. However, for simplicity, we will only shift Latin letters in a circular manner.

### Input Format

The shift size for encryption is provided.

The file _public.txt_ contains text in English.

### Output Format:

Write the encrypted text to the file _private.txt_.

### Example 1

__Input__
```plaintext
# User input
3

# Contents of public.txt
Hello, world!
```

__Output__
```plaintext
# Contents of private.txt
Khoor, zruog!
```

### Example 2

__Input__
```plaintext
# User input
-10

# Contents of public.txt
English alphabet: ABCDEFG...XYZ
```

__Output__
```plaintext
# Contents of private.txt
Udwbyix qbfxqruj: QRSTUVW...NOP
```