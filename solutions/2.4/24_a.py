n = int(input())
ENDS = " \n"
RNG = range(1, n + 1)

for i in RNG:
    for j in RNG:
        print(i * j, end=ENDS[j == n])
