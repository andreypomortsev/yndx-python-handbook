n = int(input())
neighborhoods = set()

for _ in range(n):
    neighborhoods |= set(input().split())

print(*neighborhoods, sep="\n")
