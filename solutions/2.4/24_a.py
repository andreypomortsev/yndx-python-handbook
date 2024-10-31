n = int(input())
ENDS = " \n"

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=ENDS[j == n])
