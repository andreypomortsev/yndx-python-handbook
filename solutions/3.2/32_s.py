n = int(input())
toys = []

for _ in range(n):
    str_of_toys = input().split(": ")[1]  # Удаляем имя
    set_of_toys = set(
        str_of_toys.split(", ")
    )  # Превращаем в лист и в множество
    toys += set_of_toys

counter = {}

for toy in toys:
    if toy not in counter:
        counter[toy] = 0
    counter[toy] += 1

for key, value in sorted(counter.items()):
    if value == 1:
        print(key)
