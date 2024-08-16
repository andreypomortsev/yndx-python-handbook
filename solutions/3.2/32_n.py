number_of_groceries = int(input())
groceries = set(input() for _ in range(number_of_groceries))
number_of_recipies = int(input())

recipies = []

for _ in range(number_of_recipies):
    recipie = input()
    number_of_ingredients = int(input())
    ingredients = set(input() for _ in range(number_of_ingredients))

    if ingredients.issubset(groceries):
        recipies.append(recipie)

if recipies:
    print(*sorted(recipies), sep="\n")
else:
    print("Готовить нечего")
