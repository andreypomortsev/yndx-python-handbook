import sys
from itertools import permutations

n = int(input())
if n < 3:
    sys.exit()
athletes = sorted([input() for _ in range(n)])

for top_3 in permutations(athletes, 3):
    print(", ".join(top_3))
