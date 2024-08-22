from itertools import product

num = int(input())
print("А Б В")

for a, b in product(range(1, num - 1), repeat=2):
    c = num - a - b
    if c >= 1:
        print(a, b, c)
