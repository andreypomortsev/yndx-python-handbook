size = int(input())

formatter = len(str((size + 1) // 2))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        digit = min(i, j, size - i + 1, size - j + 1)
        print(f"{digit:>{formatter}}", end=" \n"[j == size])
