n, m = int(input()), int(input())

unique_children = len({input() for _ in range(n + m)})

# Если какую-то кашу никто не любит
if not n or not m:
    print(max(n, m))

# Если группы одной длинны, которая равна кол-ву уникальных фамилий
elif unique_children == n == m:
    print("Таких нет")

# Вычитаем из уникальных фамилий не уникальные
else:
    print(unique_children - (n + m - unique_children))
