n = int(input())

line = 1
ENDS = [" ", "\n"]

for i in range(1, n + 1):
    cond = i == (line * (line + 1)) // 2
    print(i, end=ENDS[cond])
    line += cond
