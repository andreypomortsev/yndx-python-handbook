## [Детский сад — штаны на лямках](../../../solutions/2.1/21_j.py)

В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из трёх цифр:

- номер группы в саду;
- номер кроватки, закреплённой за ребёнком;
- порядковый номер ребёнка в списке группы.

Воспитатель просит сделать программу, которая по имени ребенка и номеру его шкафчика формирует «красивую» карточку для личного дела.

### Формат ввода

В первой строке записано имя ребенка.
Во второй строке записан номер шкафчика.

### Формат вывода:

Карточка в виде:

Группа №<номер группы>.  
<номер ребёнка в списке>. <имя ребенка>.  
Шкафчик: <номер шкафчика>.  
Кроватка: <номер кроватки>.

### Пример 1

__Ввод__
```plaintext
Ванечка
832
```

__Вывод__
```plaintext
Группа №8.
2. Ванечка.
Шкафчик: 832.
Кроватка: 3.
```

### Пример 2

__Ввод__
```plaintext
Машенька
141
```

__Вывод__
```plaintext
Группа №1.
1. Машенька.
Шкафчик: 141.
Кроватка: 4.
```