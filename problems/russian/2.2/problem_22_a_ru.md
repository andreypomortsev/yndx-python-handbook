## [Просто здравствуй, просто как дела](../../../solutions/2.2/22_a.py)

Умение вести диалог — важный навык для воспитанного человека.

Напишите диалоговую программу, которая сначала познакомится с пользователем, а затем поинтересуется его настроением.

### Формат ввода

В первой строке записано имя пользователя.
Во второй — ответ на вопрос: «хорошо» или «плохо».

### Формат вывода:

В первой строке должен быть вопрос «Как Вас зовут?»
Во второй строке — «Здравствуйте, %username%!»
В третьей строке — вопрос «Как дела?»
В четвёртой строке реакция на ответ пользователя:

- если пользователь ответил «хорошо», следует вывести сообщение «Я за вас рада!»;
- если пользователь ответил «плохо», следует вывести сообщение «Всё наладится!».

### Пример 1

__Ввод__
```plaintext
Аня
хорошо
```

__Вывод__
```plaintext
Как Вас зовут?
Здравствуйте, Аня!
Как дела?
Я за вас рада!
```

### Пример 2

__Ввод__
```plaintext
Боря
плохо
```

__Вывод__
```plaintext
Как Вас зовут?
Здравствуйте, Боря!
Как дела?
Всё наладится!
```