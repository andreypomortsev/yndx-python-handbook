from itertools import product

ENDS = [" ", "\n"]
n = int(input())
m = int(input())

formatter = 0
prod_n_m = n * m

while prod_n_m:
    prod_n_m //= 10
    formatter += 1

for i, j in product(range(1, n + 1), range(1, m + 1)):
    number = (i - 1) * m + j
    print(f"{number:>{formatter}}", end=ENDS[j == m])
