## [Лесенка](../../../solutions/6.1/61_j.py)

Напишите функцию `stairs`, принимающую вектор и возвращающую матрицу, в которой каждая строка является копией вектора со смещением.

### Примечание

Ваше решение должно содержать только функции.\
В решении не должно быть вызовов требуемых функций.

### Пример 1

**Ввод**
```python
print(stairs(np.arange(3)))
```

**Вывод**
```plaintext
[[0 1 2]
 [2 0 1]
 [1 2 0]]
```

### Пример 2

**Ввод**
```python
print(stairs(np.arange(5)))
```

**Вывод**
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

```python
import numpy as np
from memory_profiler import profile


# Solution using advanced indexing
@profile
def stairs_advanced(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array([row[(np.arange(n) - i)] for i in range(n)])
    return result


# Solution using np.roll
@profile
def stairs_roll(row: np.array) -> np.ndarray:
    n = row.shape[0]
    result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    return result


def test_peak_memory_usage(n: int):
    row = np.arange(n)
    print("RAM usage for the advanced indexing solution:")
    stairs_advanced(row)

    print("RAM usage for the np.roll solution:")
    stairs_roll(row)


if __name__ == "__main__":
    n = 10000
    test_peak_memory_usage(n)

```

### Результат должен выглядеть примерно так:

#### Продвинутые Индексы

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     30.9 MiB     30.9 MiB           1   @profile
     6                                         def stairs_advanced(row: np.array) -> np.ndarray:
     7     30.9 MiB      0.0 MiB           1       n = row.shape[0]
     8   1363.1 MiB   1332.2 MiB       20001       result = np.array(list(map(lambda i: row[(np.arange(n) - i) % n], range(n))))
     9   1363.1 MiB      0.0 MiB           1       return result
```

#### np.roll

```plaintext
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13    600.1 MiB    600.1 MiB           1   @profile
    14                                         def stairs_roll(row: np.array) -> np.ndarray:
    15    600.1 MiB      0.0 MiB           1       n = row.shape[0]
    16   1521.4 MiB    921.3 MiB       20001       result = np.array(list(map(lambda i: np.roll(row, shift=i), range(n))))
    17   1521.4 MiB      0.0 MiB           1       return result
```

Измерения производились на Apple MacBook Pro M1 Pro 16 Gb