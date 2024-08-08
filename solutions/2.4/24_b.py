n = int(input())

RNG = range(1, n + 1)

for i in RNG:
    for j in RNG:
        print(f"{j} * {i} = {i * j}")
