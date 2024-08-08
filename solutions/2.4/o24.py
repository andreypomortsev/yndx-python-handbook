n, m = int(input()), int(input())

ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j % 2:
            index = n * (j - 1) + i
        else:
            index = n * j - i + 1
        print(f"{index:>{formatter}}", end=ENDS[j == m])
