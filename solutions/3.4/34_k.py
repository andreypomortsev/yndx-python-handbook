from itertools import product

n, m = int(input()), int(input())
formatter = len(str(n * m))
ENDS = [" ", "\n"]

for i, j in product(range(1, n + 1), range(1, m + 1)):
    number = (i - 1) * m + j
    print(f"{number:>{formatter}}", end=ENDS[j == m])
