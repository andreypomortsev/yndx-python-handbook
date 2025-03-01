## [Новогоднее настроение 2.0](../../../solutions/2.4/24_r.py)

Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
Помогите им, написав программу, которая по введённому числу строит математическую ёлку.

### Формат ввода

Вводится одно натуральное число — количество чисел в математической ёлке.

### Формат вывода:

Требуемая новогодня ёлка.

### Пример 1

__Ввод__
```plaintext
14
```

__Вывод__
```plaintext
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
```

### Пример 2

__Ввод__
```plaintext
6
```

__Вывод__
```plaintext
  1  
 2 3 
4 5 6
```

### Подход к решению

1. **Определение количества строк ёлки:**
   - Используем формулу для вычисления треугольных чисел: $t = \frac{n \cdot (n + 1)}{2}$, где $t$ — общее количество чисел, а $n$ — количество строк.
   - Находим $n$ через обратную формулу: $n = \frac{-1 + \sqrt{1 + 8 \cdot t}}{2}$.
   - Округляем $n$ вверх до ближайшего целого числа, чтобы учесть все числа в $t$.

2. **Форматирование вывода:**
   - Для каждого числа в строке учитываем его длину, чтобы правильно выровнять числа по центру.
   - Вычисляем максимальную ширину строки (`formatter`), что обеспечивает корректное форматирование вывода.

3. **Генерация ёлки:**
   - Используем два цикла которые в сумме дают повторы от 0 до $t$.
   - Во внутреннем цикле добавляем числа последовательно в строку и на выходе из него распечатываем результат.
   - Форматируем строку с использованием ширины `formatter` для центрирования.
   - Внешний цикл отвечает за общее количество строк.
