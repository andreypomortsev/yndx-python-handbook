n = int(input())
toys = []

for _ in range(n):
    # ['Аня', 'кукла, машинка, кукла, домик']
    str_of_toys = input().split(": ")[1]  # Удаляем имя
    # {'машинка', 'кукла', 'домик'}
    # Оставляем уникальные игрушки
    set_of_toys = set(str_of_toys.split(", "))
    toys += set_of_toys

counter = {}

for toy in toys:
    if toy not in counter:
        counter[toy] = 0
    counter[toy] += 1

for key, value in sorted(counter.items()):
    if value == 1:
        print(key)
