## [Модернизация системы вывода](../../../solutions/4.1/41_f.py)

Разработайте функцию `modern_print`, которая принимает строку и выводит её, если она не была выведена ранее.

### Примечание

В решении не должно быть вызовов требуемых функций.

### Пример 1

__Ввод__
```python
modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
```

__Вывод__
```plaintext
Hello!
How do you do?
```

### Пример 2

__Ввод__
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

__Вывод__
```plaintext
Ало!
Я тебя не слышу
Позвони когда сможешь
```