n, m = int(input()), int(input())

one_porridge_lovers = set()

for _ in range(n + m):
    child = input()
    if child in one_porridge_lovers:
        one_porridge_lovers.remove(child)
    else:
        one_porridge_lovers.add(child)

if one_porridge_lovers:
    print(*sorted(one_porridge_lovers), sep="\n")
else:
    print("Таких нет")
