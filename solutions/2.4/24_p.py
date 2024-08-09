size, width = int(input()), int(input())

for i in range(1, size + 1):
    for j in range(1, size + 1):
        prod = i * j
        print(f"{prod:^{width}}", end="")
        if j < size:
            print("|", end="")
    length = size * width + size - 1
    if i < size:
        print("\n", "-" * length, sep="")
