n, m = int(input()), int(input())

ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2:
            index = m * (i - 1) + j
        else:
            index = m * i - (j - 1)
        print(f"{index:>{formatter}}", end=ENDS[j == m])
