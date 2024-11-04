n = int(input())
preferences = {}

for _ in range(n):
    line = input().split()
    # Last name -> porridge (might be plural)
    preferences[line[0]] = set(line[1:])

searching_porrigde = input()
last_names = set()

for last_name, porridge in preferences.items():
    if searching_porrigde in porridge:
        last_names.add(last_name)

if last_names:
    print(*sorted(last_names), sep="\n")
else:
    print("Таких нет")
