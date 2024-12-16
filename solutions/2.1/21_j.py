name = input()
locker = input()

group = int(locker) // 100
bed = int(locker) // 10 % 10
number = int(locker) % 10

answer = (
    f"Группа №{group}.\n"
    f"{number}. {name}.\n"
    f"Шкафчик: {locker}.\n"
    f"Кроватка: {bed}."
)

print(answer)
