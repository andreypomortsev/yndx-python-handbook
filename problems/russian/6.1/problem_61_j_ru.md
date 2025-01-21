## [Лесенка](../../../solutions/6.1/61_j.py)

Напишите функцию `stairs`, принимающую вектор и возвращающую матрицу, в которой каждая строка является копией вектора со смещением.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример 1

__Ввод__
```python
print(stairs(np.arange(3)))
```

__Вывод__
```plaintext
[[0 1 2]
 [2 0 1]
 [1 2 0]]
```

### Пример 2

__Ввод__
```python
print(stairs(np.arange(5)))
```

__Вывод__
```plaintext
[[0 1 2 3 4]
 [4 0 1 2 3]
 [3 4 0 1 2]
 [2 3 4 0 1]
 [1 2 3 4 0]]
```

## Подход к решению

Я использую [продвинутую индексацию NumPy](https://numpy.org/doc/stable/user/basics.indexing.html#advanced-indexing), чтобы создать матрицу с циклическим сдвигом элементов.

1. Сначала я создаю массив индексов от 0 до $n-1$ с помощью `np.arange(n)`.
2. Для каждого сдвига создаю массив индексов с помощью `np.arange(n) - i`, где $i$ — это количество сдвигов для каждой строки.
3. В _NumPy_ отрицательные индексы работают как индексы с конца массива, например, -1 указывает на последний элемент. Это позволяет нам циклично "обернуть" индексы.

### Почему решение работает:

- Индексация с отрицательными индексами автоматически "оборачивает" их, так что не нужно использовать дополнительные операции.
- Это решение эффективно работает для задачи, так как каждый сдвиг выполняется за постоянное время.

### Преимущество:

- Нет лишнего создания копий массива, так как индексация работает прямо с исходными данными.

### Минусы `np.roll`:

- Меньше гибкости: `np.roll` ограничен только циклическим сдвигом, а мое решение позволяет легче настроить тип сдвига, если нужно.
- Избыточность: При использовании `np.roll` каждый сдвиг требует перерасчета всего массива, что может быть менее эффективно для некоторых случаев.

### Код для проверки использования памяти

Для проверки кода убедитесь что у вас установлены:

- `numpy`
- `memory_profiler`

#### Продвинутые Индексы

```python
import numpy as np
from memory_profiler import profile


# Solution using advanced indexing
@profile
def stairs_advanced(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array([row[(np.arange(n) - i)] for i in range(n)])
    return result


if __name__ == "__main__":
    row = np.arange(10000)
    print("RAM usage for the advanced indexing solution:")
    stairs_advanced(row)

```

#### Решение с np.roll

```python
import numpy as np
from memory_profiler import profile


# Solution using np.roll
@profile
def stairs_roll(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    return result


if __name__ == "__main__":
    row = np.arange(10000)
    print("RAM usage for the np.roll solution:")
    stairs_roll(row)

```

### Результаты

#### Продвинутые Индексы

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     31.0 MiB     31.0 MiB           1   @profile
     7                                         def stairs_advanced(row: np.array) -> np.ndarray:
     8     31.0 MiB      0.0 MiB           1       n = row.shape[0]
     9   1256.9 MiB   1225.9 MiB       10001       result = np.array([row[(np.arange(n) - i)] for i in range(n)])
    10   1256.9 MiB      0.0 MiB           1       return result
```

#### np.roll

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     30.9 MiB     30.9 MiB           1   @profile
     7                                         def stairs_roll(row: np.array) -> np.ndarray:
     8     30.9 MiB      0.0 MiB           1       n = row.shape[0]
     9   1364.0 MiB   1333.1 MiB       20001       result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    10   1364.0 MiB      0.0 MiB           1       return result
```

Измерения производились на Apple MacBook Pro M1 Pro 16 Gb