n, m = int(input()), int(input())

porridge_one = {input() for _ in range(n)}
porridge_two = {input() for _ in range(m)}

length = len(porridge_one.intersection(porridge_two))

if length:
    print(length)
else:
    print("Таких нет")
