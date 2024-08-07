n = int(input())
total = 0

for _ in range(n):
    bunnies = 0
    while (word := input()) != "ВСЁ":
        bunnies += word == "зайка"
    total += bool(bunnies)

print(total)
