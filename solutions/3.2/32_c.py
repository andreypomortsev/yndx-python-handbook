n = int(input())
neighborhoods = set()

for _ in range(n):
    neighborhood = set(input().split())
    neighborhoods = neighborhoods.union(neighborhood)

print(*neighborhoods, sep="\n")
