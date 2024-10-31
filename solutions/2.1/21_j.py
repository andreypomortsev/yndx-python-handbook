name = input()
locker = input()

group = int(locker) // 100
bed = int(locker) // 10 % 10
number = int(locker) % 10

answer = f"""Группа №{group}.
{number}. {name}.
Шкафчик: {locker}.
Кроватка: {bed}."""

print(answer)
