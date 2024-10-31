n = int(input())

line = 1

for i in range(1, n + 1):
    cond = i == (line * (line + 1)) // 2
    line += cond
    print(i, end=" \n"[cond])
