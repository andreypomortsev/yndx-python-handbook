## [Файловая чистка](../../../solutions/3.5/35_i.py)

_Python_ в первую очередь скриптовый язык. Такие языки часто используются для создания консольных утилит.

Напишите простую утилиту, которая очищает заданный файл от:

- повторяющихся пробелов;
- повторяющихся символов перевода строки;
- табуляций;
- излишних пробелов в начале и конце строк.

### Формат ввода

Пользователь вводит два имени файлов.\
Входной файл содержит неформатированный текст произвольной длины.

### Формат вывода:

Во второй файл выведите очищенный текст.

### Пример

__Ввод__
```plaintext
# Пользовательский ввод:
first.txt
second.txt

# Содержимое файла first.txt
    очень 		 плохо форматированный       текст


ну		ну	
прямо

очень-очень

	
```

__Вывод__
```plaintext
# Содержимое файла second.txt
очень плохо форматированный текст
нуну
прямо
очень-очень

```