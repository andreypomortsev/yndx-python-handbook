n = int(input())
total = 0

for _ in range(n):
    bunnies = 0
    while (words := input()) != "ВСЁ":
        bunnies += words == "зайка"
    total += bool(bunnies)

print(total)
