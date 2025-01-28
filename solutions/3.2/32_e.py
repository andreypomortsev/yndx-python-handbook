n, m = int(input()), int(input())

unique_children = len({input() for _ in range(n + m)})

# Если группы одной длинны, которая равна кол-ву уникальных фамилий
# то никто не любит только одну кашу
# If groups are of the same length, which is equal to the number
# of unique surnames, then no one likes only one porridge
if unique_children == n == m:
    print("Таких нет")

# Вычитаем из уникальных фамилий не уникальные
# Subtract non-unique from unique surnames
else:
    one_porridge_lovers = 2 * unique_children - n - m
    print(one_porridge_lovers)
