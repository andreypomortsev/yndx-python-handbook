n, m = int(input()), int(input())

unique_children = len({input() for _ in range(n + m)})

# Если группы одной длинны, которая равна кол-ву уникальных фамилий
if unique_children == n == m:
    print("Таких нет")

# Вычитаем из уникальных фамилий не уникальные
else:
    print(2 * unique_children - n - m)
