## [Обобщение](../../../solutions/3.3/33_t.py)

Поздравляем, это последняя задача в подборке!
Завершим её на высокой ноте — теперь вы объедините всё, что узнали о множествах, списочных выражениях и фильтрации данных.

В этом задании вы проанализируете текст и определите пары слов, которые имеют не менее трёх общих букв.
Важно: порядок слов в паре не имеет значения, а повторяющиеся буквы не считаются несколько раз.

Вашему решению будет предоставлена переменная `text`.

Напишите выражение для генерации множества, содержащего все кортежи пар слов, имеющих более двух общих букв без учёта повторений.
Пары с разным порядком слов следует считать одной и той же и включать в результат только в одном (лексикографически упорядоченном) виде.

### Примечание

В решении не должно быть ничего, кроме выражения.

Все слова в тексте различны.

<details>
<summary><h4>Подсказка</summary>

1. Используйте вложенные в списочное выражение циклы для перебора всех пар
2. Для фильтрации преобразуйте слова в множества и найдите их пересечение
3. Сортируйте слова в кортежах для избежания повторов

</details>

### Пример 1

__Ввод__
```plaintext
text = 'ехали медведи на велосипеде'
```

__Вывод__
```plaintext
{('велосипеде', 'медведи'), ('велосипеде', 'ехали')}
```

### Пример 2

__Ввод__
```plaintext
text = 'а за ними кот задом наперед'
```

__Вывод__
```plaintext
set()
```