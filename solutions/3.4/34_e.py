groceries = []

for _ in range(3):
    line = input().split(", ")
    if line[0]:
        groceries += line

groceries.sort()

for index, item in enumerate(groceries, 1):
    print(f"{index}. {item}")
