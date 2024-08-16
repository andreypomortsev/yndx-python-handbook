n = int(input())
all_dishes = set(input() for _ in range(n))

days = int(input())
served_dishes = set()

for _ in range(days):
    number_of_dishes = int(input())
    served_dishes |= set(input() for _ in range(number_of_dishes))

dishes_left = all_dishes - served_dishes

if dishes_left:
    print(*sorted(dishes_left), sep="\n")
else:
    print("Готовить нечего")
