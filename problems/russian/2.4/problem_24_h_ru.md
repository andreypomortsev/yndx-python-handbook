## [Максимальная сумма](../../../solutions/2.4/24_h.py)

Ребята в детском саду снова играют с числами. И пусть числа они знают плохо, придумывать их они очень любят.
Они договорились, что будут называть числа по очереди и тот, кто назовёт число с наибольшей суммой цифр, будет считаться победителем. В качестве судьи они выбрали бедную воспитательницу, и она попросила нас о помощи. Напишите программу, которая определит победителя.

### Формат ввода

В первой строке записано число $N$ — количество детей в группе. Далее вводятся имя ребенка и его число (каждое на своей строке).

### Формат вывода:

Требуется вывести имя победителя.
Если два ребенка назвали числа с одинаковой суммой цифр, победителем должен быть признан тот, кто ходил позже.

### Пример 1

__Ввод__
```plaintext
2
Аня
123
Боря
234
```

__Вывод__
```plaintext
Боря
```

### Пример 2

__Ввод__
```plaintext
3
Аня
1234
Боря
234
Ваня
2323
```

__Вывод__
```plaintext
Ваня
```