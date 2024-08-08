n, m = int(input()), int(input())

ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    num = i
    for j in range(m):
        indx = j == m - 1  # Отслеживаем конец строки
        print(f"{num:>{formatter}}", end=ENDS[indx])
        num += n
