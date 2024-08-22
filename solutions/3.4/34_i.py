from itertools import product

n = int(input())
ENDS = [" ", "\n"]

for i, j in product(range(1, n + 1), repeat=2):
    print(i * j, end=ENDS[j == n])
