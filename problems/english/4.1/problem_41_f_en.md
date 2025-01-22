## [Modernizing Output System](../../../solutions/4.1/41_f.py)

Develop a function `modern_print` that takes a string and prints it if it has not been printed before.

### Note

The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
```

__Output__
```plaintext
Hello!
How do you do?
```

### Example 2

__Input__
```python
modern_print("Ало!")
modern_print("Ало!")
modern_print("Я тебя не слышу")
modern_print("Ало!")
modern_print("Ало!")
modern_print("Позвони когда сможешь")
modern_print("Позвони когда сможешь")
modern_print("Я тебя не слышу")
```

__Output__
```plaintext
Ало!
Я тебя не слышу
Позвони когда сможешь
```