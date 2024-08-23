from itertools import permutations

n = int(input())
athletes = sorted([input() for _ in range(n)])

for perm in permutations(athletes):
    print(", ".join(perm))
