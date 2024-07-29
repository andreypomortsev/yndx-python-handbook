name = input()
locker = int(input())
group = locker // 100
bed = locker // 10 % 10
number = locker % 10
answer = f"""Группа №{group}.
{number}. {name}.
Шкафчик: {locker}.
Кроватка: {bed}."""
print(answer)
